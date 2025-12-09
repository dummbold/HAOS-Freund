"""Config flow for HAOS•Freund integration."""
import json
import logging
import aiohttp
import async_timeout
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

DOMAIN = "haos_freund"

DATA_SCHEMA = vol.Schema({
    vol.Required("name"): str,
    vol.Required("url"): str,
    vol.Optional("scan_interval", default=60): vol.All(vol.Coerce(int), vol.Range(min=10)),
})

async def validate_input(hass: HomeAssistant, data: dict):
    """Validate the user input allows us to connect."""
    session = async_get_clientsession(hass)
    
    try:
        async with async_timeout.timeout(10):
            response = await session.get(data["url"])
            if response.status != 200:
                raise ValueError("HTTP Error")
            
            # Hole den kompletten Response als Text
            text = await response.text()
            
            # Finde den Anfang des body-Inhalts (nach dem schließenden >)
            body_start = text.find('<body>')
            if body_start == -1:
                raise ValueError("invalid_json")
            body_start += 6  # Länge von '<body>'
            
            # Finde das Ende
            body_end = text.find('</body>', body_start)
            if body_end == -1:
                raise ValueError("invalid_json")
            
            # Extrahiere nur den body-Inhalt
            body_content = text[body_start:body_end].strip()
            
            # Parse das als JSON
            json_data = json.loads(body_content)
            
            if not isinstance(json_data, dict):
                raise ValueError("Invalid JSON structure")
                
    except aiohttp.ClientError:
        raise ValueError("cannot_connect")
    except json.JSONDecodeError:
        raise ValueError("invalid_json")
    except Exception:
        raise ValueError("invalid_json")
    
    return {"title": data["name"]}
    
class HaosFreundConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for HAOS•Freund."""

    VERSION = 1
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                
                await self.async_set_unique_id(user_input["url"])
                self._abort_if_unique_id_configured()
                
                return self.async_create_entry(title=info["title"], data=user_input)
            except ValueError as err:
                errors["base"] = str(err)
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors
        )

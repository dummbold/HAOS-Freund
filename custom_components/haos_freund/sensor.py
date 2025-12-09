"""Sensor platform for HAOS•Freund integration."""
import json
import logging
from datetime import timedelta

import aiohttp
import async_timeout

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

DOMAIN = "haos_freund"


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up HAOS•Freund sensors from a config entry."""
    
    url = config_entry.data["url"]
    name = config_entry.data["name"]
    scan_interval = config_entry.data.get("scan_interval", 60)
    
    session = async_get_clientsession(hass)
    
    async def async_update_data():
        """Fetch data from API."""
        try:
            async with async_timeout.timeout(10):
                response = await session.get(url)
                if response.status != 200:
                    raise UpdateFailed(f"Error fetching data: {response.status}")
                
                # Hole den kompletten Response als Text
                text = await response.text()
                
                # Finde den Anfang des body-Inhalts (nach dem schließenden >)
                body_start = text.find('<body>')
                if body_start == -1:
                    raise UpdateFailed("No <body> tag found in response")
                body_start += 6  # Länge von '<body>'
                
                # Finde das Ende
                body_end = text.find('</body>', body_start)
                if body_end == -1:
                    raise UpdateFailed("No </body> tag found in response")
                
                # Extrahiere nur den body-Inhalt
                body_content = text[body_start:body_end].strip()
                
                # Parse das als JSON
                return json.loads(body_content)
                
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
        except json.JSONDecodeError as err:
            raise UpdateFailed(f"Invalid JSON: {err}")    
            
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=f"{name} coordinator",
        update_method=async_update_data,
        update_interval=timedelta(seconds=scan_interval),
    )
    
    await coordinator.async_config_entry_first_refresh()
    
    # Flatten JSON and create sensors
    sensors = []
    
    def flatten_json(data, parent_key=""):
        """Recursively flatten nested JSON."""
        items = []
        for key, value in data.items():
            new_key = f"{parent_key}_{key}" if parent_key else key
            
            if isinstance(value, dict):
                items.extend(flatten_json(value, new_key))
            else:
                items.append((new_key, value))
        return items
    
    flattened = flatten_json(coordinator.data)
    
    for sensor_key, _ in flattened:
        sensors.append(
            HaosFreundSensor(
                coordinator=coordinator,
                config_entry=config_entry,
                sensor_key=sensor_key,
                device_name=name,
            )
        )
    
    async_add_entities(sensors)


class HaosFreundSensor(CoordinatorEntity, SensorEntity):
    """Representation of a HAOS•Freund Sensor."""

    def __init__(self, coordinator, config_entry, sensor_key, device_name):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._sensor_key = sensor_key
        self._device_name = device_name
        self._config_entry = config_entry
        
        self._attr_name = f"{device_name} {sensor_key.replace('_', ' ').title()}"
        self._attr_unique_id = f"{config_entry.entry_id}_{sensor_key}"
    
    @property
    def native_value(self):
        """Return the state of the sensor."""
        def get_nested_value(data, key):
            """Get value from flattened key."""
            keys = key.split("_")
            value = data
            for k in keys:
                if isinstance(value, dict):
                    value = value.get(k)
                else:
                    return None
            return value
        
        return get_nested_value(self.coordinator.data, self._sensor_key)
    
    @property
    def device_info(self):
        """Return device information."""
        return {
            "identifiers": {(DOMAIN, self._config_entry.entry_id)},
            "name": self._device_name,
            "manufacturer": "HAOS•Freund",
            "model": "Generic JSON Device",
        }

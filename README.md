>🇺🇸🇬🇧🇫🇷🇪🇸🇮🇹🇪🇺🇺🇦🇦🇺🇫🇮🇨🇿🇧🇷🇨🇦🇰🇿🇨🇴🇲🇶🇳🇬🇸🇨🇪🇭🇺🇾🇺🇬🏳️🏴‍☠️
>
>‼️ **Non german users:** please use your browsers translation function to translate this page into your prefered language. It is written in german – one of the languages with the most complex structures. Translation FROM german INTO another language is mostly some sort of linguistic "downscaling" and you should read theese textes in nearly native foreign language. 
>
>Thanks for your cooperation and let me know in the "Issues" if and how this works for your language.


# HAOS•Freund

### Eine universelle Homeassistant Integration für Endgeräte mit .JSON

<img src="images/FREUND-LOGO-sg.svg" width="561" />

Der HAOS•Freund ist eine Integration für Homeassistant (HAOS). Und sie löst ein eklatantes Problem: bisher musste man nämlich für JSON-Ausgaben die Sensoren von Hand in der configuration.yaml eintragen. Diese Zeiten sind nunmehr vorbei!

Zur Installation muss man in HAOS ein Terminal installiert haben (AddOn: Terminal&SSH) und folgendes in die Shell eingeben:

    cd /config
    git clone https://github.com/dummbold/haos-freund.git
    cp -r haos-freund/custom_components/haos_freund custom_components/

**Anschließend HAOS neu starten (voller Neustart!)!**

Am Besten nochmal nachschauen ob folgende Verzeichnisse angelegt wurden:

    ls -la                   -> Die Originaldateien im Verzeichnis /config/haos-freund
    ls -la custom_components -> Die Installation im Verzeichnis /config/custom_components/haos_freund

Dann kann man in "+ Integration hinzufügen" nach "haos" suchen und findet den HAOS•Freund.

**Eintragungen in der Maske:**
- Gerätename: ein beliebiger Name
- Geräte IP: nicht den Pfad zur JSON vergessen (z.B. **192.172.166.23/json**)!!!
- Update: Update der Daten in Sekunden

In der aktuellen Version kann der HAOS•Freund auch JSON lesen das in HTML eingebettet ist und er entfernt dabei sämtliche Timestamps. Die benötigt HAOS nicht. Einschränkung: Die Timestamps müssen durch **_ts** markiert sein. Die Tatsache, dass JSON ein sehr offenes Format ist macht die Erkennung und das Parsen von JSON-Einträgen schwierig. Eine Idee für die Lösung des Problems reift bereits.

Den Rest macht die Integration. Sie liest das JSON aus, parst es und legt in der Integration das Gerät und für jeden Wert im JSON eine Entität an. Das Gerät erscheint dann in der Integration und kann verwaltet werden. Nicht benutzte Entitäten kann man einfach deaktivieren. Einheiten werden aktuell noch nicht berücksichtigt - das kommt aber noch.

<img width="1314" height="877" alt="integration" src="https://github.com/user-attachments/assets/0c544cdc-16f2-4716-a40a-32fa80ae82db" />

Die Integration sollte eigentlich universell für alle Geräte einsetzbar sein für die es keine Integration gibt, die aber ein JSON zur Verfügung stellen. Postet gerne im Forumsbereich ob es geklappt hat und welche Geräte ihr damit eingebunden habt.



>🇺🇸🇬🇧🇫🇷🇪🇸🇮🇹🇪🇺🇺🇦🇦🇺🇫🇮🇨🇿🇧🇷🇨🇦🇰🇿🇨🇴🇲🇶🇳🇬🇸🇨🇪🇭🇺🇾🇺🇬🏳️🏴‍☠️
>
>‼️ **Non german users:** please use your browsers translation function to translate this page into your prefered language. It is written in german – one of the languages with the most complex structures. Translation FROM german INTO another language is mostly some sort of linguistic "downscaling" and you should read theese textes in nearly native foreign language. 
>
>Thanks for your cooperation and let me know in the "Issues" if and how this works for your language.


# HAOS•Freund

### Eine universelle Homeassistant Integration für Endgeräte mit .JSON

<img src="images/FREUND-LOGO-sg.svg" width="561" />

Der HAOS•Freund ist eine Integration für Homeassistant (HAOS).

Zur Installation kann man die .ZIP-Datei laden und alles manuell installieren oder ganze einfach in HAOS ein Terminal installieren, starten und folgendes in die Shell eingeben:

    cd /config
    git clone https://github.com/dummbold/haos-freund.git
    cp -r haos-freund/custom_components/haos_freund custom_components/

**Anschließend HAOS neu starten**! Und nachschauen ob folgende Verzeichnisse angelegt wurden:

    /config/custom_components/haos_freund       -> Die Installation
    /config/haos-freund                         -> Die Originaldateien

Dann kann man in den Integrationen nach "haos" suchen und findet den HAOS•Freund.

Beim Eintragen der Geräte IP nicht den Pfad zur JSON vergessen (z.B. **192.172.166.23/json**)!!!

In der aktuellen Version kann der HAOS•Freund auch JSON lesen das in HTML eingebettet ist und er entfernt sämtlich Timestamps. Die benötigt HAOS nicht. Einschränkung: Die Timestamps müssen durch _ts markiert sein. Die Tatsache, dass JSON ein sehr offenes Format ist macht die Erkennung von JSON-Einträgen schwierig. Eine Idee für die Lösung des Problems reift bereits.

Man kann dann ein neues Gerät anlegen, die IP-Adresse zum JSON auswählen .... und den Rest macht die Integration. Sie liest das JSON aus, parst es und legt für jeden Wert im JSON eine Entität an. Das Gerät erscheint dann in der Intgration und kann verwaltet werden. Nicht benutzte Entitäten kann man einfach deaktivieren.

Die Integration sollte eigentlich universell für alle Geräte einsetzbar sein für die es keine Integration gibt, die aber ein JSON zur Verfügung stellen. Postet gerne im Forumsbereich welche Geräte ihr damit eingebunden habt.



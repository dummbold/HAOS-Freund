    🇺🇸🇬🇧🇫🇷🇪🇸🇮🇹🇪🇺🇺🇦🇦🇺🇫🇮🇨🇿🇧🇷🇨🇦🇰🇿🇨🇴🇲🇶🇳🇬🇸🇨🇪🇭🇺🇾🇺🇬🏳️🏴‍☠️
    ‼️ Non german users: please use your browsers translation function to translate this page 
    into your prefered language. It is written in german – one of the languages with the most 
    complex structures. Translation FROM german INTO another language is mostly some sort of 
    linguistic "downscaling" and you should read theese textes in nearly native foreign language. 
    Thanks for you cooperation and let me know in the "Issues" if and how this works for your language.


# HAOS•Freund

### Eine universelle Homeassistant Integration für Endgeräte mit .JSON

<img src="images/FREUND-LOGO-sg.svg" width="561" />

Der HAOS•Freund ist eine Integration für Homeassistant (HAOS).

Zur Installation kann man die .ZIP-Datei laden und alles manuell installieren oder ganze einfach in HAOS ein Terminal installieren, starten und folgendes in die Shell eingeben:

    cd /config
    git clone https://github.com/deinname/json-freund.git
    cp -r json-freund/custom_components/json_freund custom_components/

Man kann dann ein neues Gerät anlegen, die IP-Adresse zum JSON auswählen .... und den Rest macht die Integration. Sie liest das JSON aus, parst es und legt für jeden Wert im JSON eine Entität an. Das Gerät erscheint dann in der Intgration und kann verwaltet werden. Nicht benutzte Entitäten kann man einfach deaktivieren.

Die Integration sollte eigentlich universell für alle Geräte einsetzbar sein für die es keine Integration gibt, die aber ein JSON zur Verfügung stellen. Postet gerne im Forumsbereich welche Geräte ihr damit eingebunden habt.



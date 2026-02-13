# Gebruiksaanwijzing – main.py
### Werkt alleen op Raspberry Pi!!
om code te gebruiken kies `no-gpiozero` branch.

## Installatie



Clone de repository:

`git clone https://github.com/killua-krytoi/yolov8nphone`

`cd yolov8nphone`

Installeer de afhankelijkheden:

`pip install -r requirements.txt`

## Uitvoeren

Start het script met:

`python main.py`

## Aanbevolen

Gebruik bij voorkeur een virtuele omgeving:

`source venv/bin/activate`


Installeer daarna opnieuw de dependencies en voer het script uit.

##Wat doet het systeem?

De camera staat continu aan.
Het programma leest steeds beelden van de camera.

Een AI-model bekijkt de beelden.
Het gebruikt het model YOLOv8 (een systeem voor beeldherkenning) om te controleren of er een mobiele telefoon zichtbaar is in het beeld.

Niet elk beeld wordt gecontroleerd.
Om het systeem sneller te maken, wordt slechts 1 van elke 10 beelden geanalyseerd.

Detectie van een telefoon.

Als er een mobiele telefoon wordt herkend, start een timer.

Zodra de ingestelde tijd is bereikt (hier staat die op 0 seconden), gebeurt het volgende:

De LED gaat aan.

De buzzer begint te piepen.

Geen telefoon meer zichtbaar?

De timer wordt gereset.

De LED gaat uit.

De buzzer stopt.

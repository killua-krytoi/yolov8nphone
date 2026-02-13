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

## Wat doet het systeem?

Code gebruikt AI model YOLOv8 die kan objecten detecten, maar code zoek alleen voor telefoon (ID = 67).

Doordat raspberry pi 4 is niet zo sterk, ik moest code optimiseren. Op deze moment code maakt vaste resolutie van 320px320p, en stuurt naar ai alleen maar elke tiende frame.

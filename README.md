# Gebruiksaanwijzing – main.py
### Waarshuwing
Deze code werkt alleen op RaspberryPi, om code te gebruiken op Windows/MacOS kies `no-gpiozero` branch.

Als code werkt niet of u heeft bugs, probeer dan om code te kopieren van `legacy` branch.

## Installatie



Kopier de repository:

`git clone https://github.com/killua-krytoi/yolov8nphone`

`cd yolov8nphone`

Installeer de afhankelijkheden:

`pip install -r requirements.txt`

of

`pip3 install -r requirements.txt`

## Uitvoeren

Start het script met:

`python main.py`

## Aanbevolen

Gebruik bij voorkeur een virtuele omgeving:

`source venv/bin/activate`


Installeer daarna opnieuw de dependencies en voer het script uit.

## Wat doet het systeem?

[Code gebruikt](https://github.com/killua-krytoi/yolov8nphone/blob/main/data/config.py#L8) AI model (YOLOv8)[https://github.com/ultralytics/ultralytics] die kan objecten detecten, maar code zoekt [alleen voor telefoon (ID = 67).](https://github.com/killua-krytoi/yolov8nphone/blob/main/data/config.py#L10)

Doordat raspberry pi 4 is niet zo sterk, ik moest code optimiseren. Op deze moment code maakt vaste [resolutie van 320px320p](https://github.com/killua-krytoi/yolov8nphone/blob/main/data/config.py#L21-#L23), en stuurt naar ai alleen maar [elke tiende frame.](https://github.com/killua-krytoi/yolov8nphone/blob/main/main.py#L16-#L18)

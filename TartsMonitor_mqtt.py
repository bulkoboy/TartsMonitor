#! /usr/bin/python3
"""


"""
__version__ = "21.10.04a"


import paho.mqtt.client as mqtt
import json


broker = "rasp4-1"
subscription = "sensor/TEMPERATURE/#"
location = {
    "T5YDNG": "Living Room",
    "T5YDFN": "Master",
    "T5YDNO": "Attic",
    "T5YDFF": "Spare",
    "T5YDOS": "Garage",
    "T5YDN8": "Closet",
}


def on_message(client: mqtt.Client, userdata: str, msg: mqtt.MQTTMessage) -> None:
    print(f"{msg.topic} {repr(msg.payload)}")


def main() -> None:
    client = mqtt.Client()
    # client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, 1883, 60)
    client.subscribe(subscription)

    client.loop_forever()

    """
    data = socket.recv_json()
    #print(data)
    data_s = "{},{},{},{},{}".format(data["time"], data["sensor"], data["type"], data["battery"], data["fvalue"])
    fahrenheit = "{:0.1f} F".format(data['value'] / 10 * (9 / 5) + 32.0)
    print(data_s, "-", fahrenheit, "-", location[data["sensor"]])
    """


if __name__ == "__main__":
    main()

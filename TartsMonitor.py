#! /usr/bin/python3
"""


"""
__version__ = "0.0.dev1"
import zmq
import json

collect_engine = "192.168.1.72"
port = 5559

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
socket.connect("tcp://{}:{}".format(collect_engine, port))

TartsDict = {
    "T5YDNG": {
        "lastTime": 0,
        "lastBattery": 0.0,
        "batteryAlarm": False,
        "timeAlarm": False,
    },
    "T5YDFN": {
        "lastTime": 0,
        "lastBattery": 0.0,
        "batteryAlarm": False,
        "timeAlarm": False,
    },
    "T5YDNO": {
        "lastTime": 0,
        "lastBattery": 0.0,
        "batteryAlarm": False,
        "timeAlarm": False,
    },
    "T5YDFF": {
        "lastTime": 0,
        "lastBattery": 0.0,
        "batteryAlarm": False,
        "timeAlarm": False,
    },
}

location = {
    "T5YDNG": "Living Room",
    "T5YDFN": "Master",
    "T5YDNO": "Attic",
    "T5YDFF": "Spare",
    "T5YDOS": "Garage",
    "T5YDN8": "Closet",
}


while True:
    data = socket.recv_json()
    # print(data)
    data_s = "{},{},{},{},{}".format(
        data["time"], data["sensor"], data["type"], data["battery"], data["fvalue"]
    )
    fahrenheit = "{:0.1f} F".format(data["value"] / 10 * (9 / 5) + 32.0)
    print(data_s, "-", fahrenheit, "-", location[data["sensor"]])

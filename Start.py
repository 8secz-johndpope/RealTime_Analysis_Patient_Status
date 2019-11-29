import os
import json
from threading import Timer

import tkinter as tk


def instant():
   os.system("python functionPanel.py")


def TimerStart():
    t = Timer(5.0, instant)
    t.start()  # after 5 seconds, "hello, world" will be printed


def loadConfigurationFile():
    from pprint import pprint

    with open('configuration.json') as f:
        data = json.load(f)

    ActionsList=data["Tools"]["Rekognition"]

    # getting length of list
    length = len(ActionsList)

    # Iterating the index
    # same as 'for i in range(len(list))'
    for i in range(length):
        Action=ActionsList[i]['action']
        if (Action=="StatusAnalysis"):
                 TimerStart()




loadConfigurationFile()











#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from src.Models.DisplayLayouts import DisplayLayouts


class DisplayConfiguration(object):
    id = 0
    device = ""
    layout = 0
    streams = list()
    screenDescription = ""

    def __init__(self, displayID: int = 0,
                 deviceID: str = "", layoutID: int = 0,
                 screenDescription: str = ""):
        self.id = displayID
        self.device = deviceID
        self.layout = DisplayLayouts(layoutID)
        self.screenDescription = screenDescription

    def __str__(self):
        retValue = "Display ID: " + self.id
        retValue += "Device: " + self.device
        retValue += "Device layout: " + self.layout
        retValue += "Streams: " + json.dumps(self.streams)
        retValue += "Screen description: " + json.dumps(self.screenDescription)
        return retValue

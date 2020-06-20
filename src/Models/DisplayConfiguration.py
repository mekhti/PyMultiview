#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from src.Models.DisplayLayouts import DisplayLayouts


class DisplayConfiguration:
    id = 0
    device = ""
    layout = 0
    streams = list()

    def __init__(self, displayID = 0, deviceID = "", layoutID = 0):
        self.id = displayID
        self.device = deviceID
        self.layout = DisplayLayouts(layoutID)

    def __str__(self):
        retValue = "Display ID: " + self.id
        retValue += "Device: " + self.device
        retValue += "Device layout: " + self.layout
        retValue += "Streams: " + json.dumps(self.streams)
        return retValue

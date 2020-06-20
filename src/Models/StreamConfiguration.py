#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.Models.StreamTypes import StreamTypes


class StreamConfiguration():
    sID = 0
    sType = StreamTypes()
    sURI = ""
    streamName = ""
    description = ""

    def __init__(self, streamID, streamType, streamURI):
        self.sID = streamID
        self.sType = streamType
        self.sURI = streamURI

    def __str__(self):
        retValue = "Stream id: " + self.sID + "\n"
        retValue += "Stream type: " + self.sType + "\n"
        retValue += "Stream URI: " + self.sURI
        return retValue

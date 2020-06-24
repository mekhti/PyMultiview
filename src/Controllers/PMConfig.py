#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from src.Models.AppConfiguration import AppConfiguration
from src.Models.StreamConfiguration import StreamConfiguration
from src.Models.DisplayConfiguration import DisplayConfiguration


class PMConfig:
    configFileName = ""
    displays = list()
    streams = list()

    def __init__(self, filename: str ="conf/pymultiview.json"):
        self.configFileName = filename
        self.readConfig()

    def readConfig(self):
        with open(self.configFileName) as jsonContentOfConfig:
            configData = json.load(jsonContentOfConfig)

            # TODO: Implement application configuration parsing
            self.appConfiguration = AppConfiguration() #configData['AppConfiguration']

            for nextDisplay in configData['Displays']:
                currentDisplay = DisplayConfiguration(displayID=nextDisplay['id'],
                                                      deviceID=nextDisplay['device'],
                                                      layoutID=nextDisplay['layoutID'])
                for nStream in nextDisplay['streams']:
                    currentDisplay.streams.append(nStream)

                self.displays.append(currentDisplay)
                currentDisplay = None

            for nextStream in configData['Streams']:
                currentStream = StreamConfiguration(streamID=nextStream['id'],
                                                    streamType=nextStream['type'],
                                                    streamURI=nextStream['streamURI'],
                                                    streamName=nextStream['streamName'],
                                                    description=nextStream['description'])
                self.streams.append(currentStream)
                currentStream=None

    def writeConfig(self):
        pass

    def reloadConfig(self):
        self.appConfiguration = None
        self.streams.clear()
        self.displays.clear()
        self.readConfig()

    def getConfigAsText(self) -> str:
        fileDescriptor = open(self.configFileName, 'r')
        return fileDescriptor.read()

    def saveConfigAsText(self, configAsText: str):
        fileDescriptor = open(self.configFileName, 'w')
        fileDescriptor.write(configAsText)
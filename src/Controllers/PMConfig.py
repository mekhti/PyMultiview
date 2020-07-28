#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from uuid import uuid4
from src.Models.AppConfiguration import AppConfiguration
from src.Models.StreamConfiguration import StreamConfiguration
from src.Models.DisplayConfiguration import DisplayConfiguration


class PMConfig:
    objectID = None
    configFileName = ""
    appConfiguration = dict()
    displays = list()
    streams = list()

    def __init__(self, filename: str ="conf/pymultiview.json"):
        self.objectID = uuid4()
        self.configFileName = filename
        self.readConfig()

    def readConfig(self):
        with open(self.configFileName, 'r', encoding='utf-8') as jsonContentOfConfig:
            configData = json.load(jsonContentOfConfig)
            self.appConfiguration = AppConfiguration(playerBackend=configData['AppConfiguration']['PlayerBackend'])

            for nextDisplay in configData['Displays']:
                currentDisplay = DisplayConfiguration(displayID=nextDisplay['id'],
                                                      deviceID=nextDisplay['device'],
                                                      layoutID=nextDisplay['layoutID'],
                                                      screenDescription=nextDisplay['screenDescription'])
                for nStream in nextDisplay['streams']:
                    currentDisplay.streams.append(nStream)

                self.displays.append(currentDisplay)
                del currentDisplay

            for nextStream in configData['Streams']:
                currentStream = StreamConfiguration(streamID=nextStream['id'],
                                                    streamType=nextStream['type'],
                                                    streamURI=nextStream['streamURI'],
                                                    streamName=nextStream['streamName'],
                                                    description=nextStream['description'])
                self.streams.append(currentStream)
                del currentStream

    def writeConfig(self):
        pass

    def reloadConfig(self):
        self.appConfiguration = None
        self.streams.clear()
        self.displays.clear()
        self.readConfig()

    def getConfigAsText(self) -> str:
        fileDescriptor = open(self.configFileName, 'r', encoding='utf-8')
        fileContent = fileDescriptor.read()
        fileDescriptor.close()
        return fileContent

    def saveConfigAsText(self, configAsText: str):
        fileDescriptor = open(self.configFileName, 'w', encoding='utf-8')
        fileDescriptor.write(configAsText)
        fileDescriptor.close()

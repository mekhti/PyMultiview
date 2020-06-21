#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.Models.StreamTypes import StreamTypes


class StreamConfiguration():
    sID = 0
    sType = None
    sURI = ""
    sName = ""
    sDescription = ""

    def __init__(self, streamID: int =0,
                 streamType: StreamTypes = StreamTypes.FILE,
                 streamURI: str = "",
                 streamName: str = "",
                 description: str = ""):
        self.sID = streamID
        self.sType = self.setStreamType(streamType)
        self.sURI = streamURI
        self.sName = streamName
        self.sDescription = description

    def __str__(self):
        retValue = "Stream id: " + self.sID + "\n"
        retValue += "Stream type: " + self.sType + "\n"
        retValue += "Stream URI: " + self.sURI
        return retValue

    def setStreamType(self, streamType):
        if type(streamType) is None:
            return StreamTypes.FILE
        elif type(streamType) is int:
            return self.getByIndexAsStr(str(streamType))
        elif type(streamType) is str:
            return self.getByStr(streamType)
        elif type(streamType) is StreamTypes:
            return streamType

    def getByStr(self, tStr: str):
        return {
            'FILE': StreamTypes.FILE,
            'UDP': StreamTypes.UDP,
            'TCP': StreamTypes.TCP,
            'RTP': StreamTypes.RTP,
            'HTTP': StreamTypes.HTTP,
            'HTTPS': StreamTypes.HTTPS,
            'RTSP': StreamTypes.RTSP,
            'RTMP': StreamTypes.RTMP,
            'HLS': StreamTypes.HLS,
            'MPEGDASH': StreamTypes.MPEGDASH,
            'DVB': StreamTypes.DVB,
            'DVBS': StreamTypes.DVBS,
            'DVBS2': StreamTypes.DVBS2,
            'DVBT': StreamTypes.DVBT,
            'DVBT2': StreamTypes.DVBT2,
            'DVBC': StreamTypes.DVBC,
            'DVBC2': StreamTypes.DVBC2
        }[tStr]

    def getByIndexAsStr(self, tIndex: str):
        return {
            '0': StreamTypes.FILE,
            '1': StreamTypes.UDP,
            '2': StreamTypes.TCP,
            '3': StreamTypes.RTP,
            '4': StreamTypes.HTTP,
            '5': StreamTypes.HTTPS,
            '6': StreamTypes.RTSP,
            '7': StreamTypes.RTMP,
            '8': StreamTypes.HLS,
            '9': StreamTypes.MPEGDASH,
            '10': StreamTypes.DVB,
            '11': StreamTypes.DVBS,
            '12': StreamTypes.DVBS2,
            '13': StreamTypes.DVBT,
            '14': StreamTypes.DVBT2,
            '15': StreamTypes.DVBC,
            '16': StreamTypes.DVBC2
        }[tIndex]

    @staticmethod
    def getByIndexInt(self, tIndex: int):
        return {
            0: StreamTypes.FILE,
            1: StreamTypes.UDP,
            2: StreamTypes.TCP,
            3: StreamTypes.RTP,
            4: StreamTypes.HTTP,
            5: StreamTypes.HTTPS,
            6: StreamTypes.RTSP,
            7: StreamTypes.RTMP,
            8: StreamTypes.HLS,
            9: StreamTypes.MPEGDASH,
            10: StreamTypes.DVB,
            11: StreamTypes.DVBS,
            12: StreamTypes.DVBS2,
            13: StreamTypes.DVBT,
            14: StreamTypes.DVBT2,
            15: StreamTypes.DVBC,
            16: StreamTypes.DVBC2
        }[tIndex]
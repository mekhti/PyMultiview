#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
uriType = {
            StreamTypes.HTTP: self.__checkHTTPS__(),
            StreamTypes.HTTPS: self.__checkHTTPS__(),
            StreamTypes.HLS: self.__checkHLS__(),
            StreamTypes.RTSP: self.__checkRTSP__(),
            StreamTypes.RTMP: self.__checkRTMP__(),
            StreamTypes.MPEGDASH: self.__checkMPEGDASH__(),
            StreamTypes.TCP: self.__checkTCP__(),
            StreamTypes.RTP: self.__checkRTP__(),
            StreamTypes.UDP: self.__checkUDP__()
        }
        print("Return value: ", uriType.get(self.inputStream.sType, False))
        return {
            StreamTypes.HTTP: self.__checkHTTPS__(),
            StreamTypes.HTTPS: self.__checkHTTPS__(),
            StreamTypes.HLS: self.__checkHLS__(),
            StreamTypes.RTSP: self.__checkRTSP__(),
            StreamTypes.RTMP: self.__checkRTMP__(),
            StreamTypes.MPEGDASH: self.__checkMPEGDASH__(),
            StreamTypes.TCP: self.__checkTCP__(),
            StreamTypes.RTP: self.__checkRTP__(),
            StreamTypes.UDP: self.__checkUDP__()
        }[self.inputStream.sType]
        return uriType.get(self.inputStream.sType, False)

"""
import requests
from uuid import uuid4
from requests.adapters import HTTPAdapter
from src.Models.StreamConfiguration import StreamConfiguration, StreamTypes
from PySide2.QtCore import QObject


class LinkChecker(QObject):
    objectID = uuid4()
    inputStream = None

    def __init__(self, inputStream: StreamConfiguration = None):
        super(LinkChecker, self).__init__()
        if inputStream is not None:
            self.setInputStream(inputStream)

    def setInputStream(self, inputStream: StreamConfiguration):
        self.inputStream = inputStream

    def getInputStream(self) -> StreamConfiguration:
        return self.inputStream

    def dispatcher(self):
        if self.inputStream.sType == StreamTypes.HTTP:
            return self.__checkHTTPS__()
        elif self.inputStream.sType == StreamTypes.HTTPS:
            return self.__checkHTTPS__()
        elif self.inputStream.sType == StreamTypes.HLS:
            # return self.__checkHLS__()
            # Temporary HLS stream checker same as HTTPS
            # TODO: revert back checking over __checkHLS__ method after implementation
            return self.__checkHTTPS__()
        elif self.inputStream.sType == StreamTypes.RTSP:
            return self.__checkRTSP__()
        elif self.inputStream.sType == StreamTypes.RTMP:
            return self.__checkRTMP__()
        elif self.inputStream.sType == StreamTypes.MPEGDASH:
            return self.__checkMPEGDASH__()
        elif self.inputStream.sType == StreamTypes.TCP:
            return self.__checkTCP__()
        elif self.inputStream.sType == StreamTypes.RTP:
            return self.__checkRTP__()
        elif self.inputStream.sType == StreamTypes.UDP:
            return self.__checkUDP__()
        else:
            return False

    def __checkHTTPS__(self) -> bool:
        session = requests.Session()
        session.mount('http://', HTTPAdapter(max_retries=1))
        try:
            r = session.get(self.inputStream.sURI)
            session.close()
        except requests.ConnectionError:
            return False

        rO = {200: True}
        return rO.get(r.status_code, False)

    def __checkHLS__(self) -> bool:
        return True

    def __checkRTMP__(self) -> bool:
        return True

    def __checkRTSP__(self) -> bool:
        return True

    def __checkMPEGDASH__(self) ->bool:
        return True

    def __checkTCP__(self) -> bool:
        return True

    def __checkRTP__(self) -> bool:
        return True

    def __checkUDP__(self) -> bool:
        return True

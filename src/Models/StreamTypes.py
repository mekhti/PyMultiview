#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class StreamTypes(Enum):
    FILE = 0
    UDP = 1
    TCP = 2
    RTP = 3
    HTTP = 4
    HTTPS = 5
    RTSP = 6
    RTMP = 7
    HLS = 8
    MPEGDASH = 9
    DVB = 10
    DVBS = 11
    DVBS2 = 12
    DVBT = 13
    DVBT2 = 14
    DVBC = 15
    DVBC2 = 16

    def __init__(self, streamType = FILE):
        self.value = streamType

    def __str__(self):
        return '{0}'.format(self.value)

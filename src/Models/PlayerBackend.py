#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class PlayerBackend(Enum):
    AUTO = 0
    GTOOLKIT = 1
    STANDART_PLAYER = 2
    FFPLAYER = 3
    GSTREAMER = 4

    def __str__(self):
        return '{0}'.format(self.value)
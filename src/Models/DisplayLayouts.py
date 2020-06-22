#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from enum import Enum, unique


@unique
class DisplayLayouts(Enum):
    L_1x1 = 0
    L_2x2 = 1
    L_3x2 = 2
    L_3x3 = 3
    L_4x3 = 4
    L_5x4 = 5
    L_6x5 = 6

    def __str__(self):
        return '{0}'.format(self.value)

    def getHCellCount(self, layout: int):
        return {
            0: 1,
            1: 2,
            2: 3,
            3: 3,
            4: 4,
            5: 5,
            6: 6
        }[layout]

    def getVCellCount(self, layout: int):
        return {
            0: 1,
            1: 2,
            2: 2,
            3: 3,
            4: 3,
            5: 4,
            6: 5
        }[layout]


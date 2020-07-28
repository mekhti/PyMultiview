#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from src.Models.PlayerBackend import PlayerBackend


class AppConfiguration(object):
    playerBackend = None

    def getByStr(self, tStr: str):
        return {
            'AUTO': PlayerBackend.AUTO,
            'GTOOLKIT': PlayerBackend.GTOOLKIT,
            'STANDART_PLAYER': PlayerBackend.STANDART_PLAYER,
            'FFPLAYER': PlayerBackend.FFPLAYER,
            'GSTREAMER': PlayerBackend.GSTREAMER
        }[tStr]

    def getByIndexAsStr(self, tIndex: str):
        return {
            '0': PlayerBackend.AUTO,
            '1': PlayerBackend.GTOOLKIT,
            '2': PlayerBackend.STANDART_PLAYER,
            '3': PlayerBackend.FFPLAYER,
            '4': PlayerBackend.GSTREAMER
        }[tIndex]

    def setPlayerBackend(self, playerBackend):
        if type(playerBackend) is None:
            return PlayerBackend.STANDART_PLAYER
        elif type(playerBackend) is int:
            return self.getByIndexAsStr(str(playerBackend))
        elif type(playerBackend) is str:
            return self.getByStr(playerBackend)
        elif type(playerBackend) is PlayerBackend:
            return playerBackend

    def __init__(self, playerBackend: PlayerBackend = PlayerBackend.STANDART_PLAYER):
        self.playerBackend = self.setPlayerBackend(playerBackend)

        # TODO: Make analizing of local system capability and chose backend based on that analizys
        # FIXME: For now, it just switch to STANDART_PLAYER backend when AUTO was chosen
        if self.playerBackend == PlayerBackend.AUTO:
            self.playerBackend = PlayerBackend.STANDART_PLAYER

    def __str__(self):
        return json.dumps(self)

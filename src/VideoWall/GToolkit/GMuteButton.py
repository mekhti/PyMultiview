#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap, QMouseEvent

from src.VideoWall.GToolkit.GPlayer import GPlayer


class GMuteButton(QLabel):
    objectID = None

    def __init__(self, parentPlayer: GPlayer):
        super(GMuteButton, self).__init__()
        self.objectID = uuid4()
        self.parentPlayer = parentPlayer
        self.setPixmap(QPixmap("img/mute-red.png"))
        self.setStyleSheet(
            "QLabel { background-color: rgba(255, 255, 255, 0);}"
        )

    def mousePressEvent(self, ev: QMouseEvent):
        if self.parentPlayer.isMuted():
            self.setPixmap(QPixmap("img/unmute-green.png"))
        else:
            self.setPixmap(QPixmap("img/mute-red.png"))
        self.parentPlayer.muteSwitch()

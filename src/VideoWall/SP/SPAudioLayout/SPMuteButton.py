#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap, QMouseEvent
from PySide2.QtCore import QSize


class SPMuteButton(QLabel):
    """
    SPMuteButton(parentSize: QSize)
    """
    objectID = uuid4()
    parentSize = None
    mutedPixmap = None
    unmutedPixmap = None
    coefficient = 0.05

    def __initPixmap__(self):
        buttonWH = self.parentSize.width() * self.coefficient
        self.mutedPixmap = QPixmap("img/mute-red.png").scaled(buttonWH, buttonWH)
        self.unmutedPixmap = QPixmap("img/unmute-green.png").scaled(buttonWH, buttonWH)

    def __init__(self, parentSize: QSize):
        super(SPMuteButton, self).__init__()
        self.parentSize = parentSize
        self.__initPixmap__()
        self.setStyleSheet(
            "QLabel { background-color: rgba(255, 255, 255, 0);}"
        )
        self.setPixmap(self.mutedPixmap)
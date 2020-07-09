#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QPushButton, QStyle
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtCore import Slot, Qt

from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget


class MuteButton(QPushButton):
    objectID = uuid4()

    def __init__(self, parentPlayerWidget: SinglePlayerWidget,
                 widgetWidth: int, widgetHeight: int):
        super(MuteButton, self).__init__()
        self.parentPlayerWidget = parentPlayerWidget
        self.widgetWidth = widgetWidth
        self.widgetHeight = widgetHeight

        self.setFixedSize(self.widgetWidth, self.widgetHeight)
        self.setFlat(False)
        self.semaphore = False

        self.muteIconPixmap = QPixmap("img/mute-red.png").scaled(self.widgetWidth, self.widgetHeight,
                                                                 Qt.AspectRatioMode.KeepAspectRatio)
        self.muteIcon = QIcon(self.muteIconPixmap)

        self.unmuteIconPixmap = QPixmap("img/unmute-green.png").scaled(self.widgetWidth, self.widgetHeight,
                                                                       Qt.AspectRatioMode.KeepAspectRatio)
        self.unmuteIcon = QIcon(self.unmuteIconPixmap)
        self.setAutoFillBackground(True)
        self.buttonStyleAsText = """
            QPushButton {
                background-color: rgba(255, 255, 255, 0); 
                border: 0px;
                border-width: 0px; 
                border-color: transparent; 
                border-radius: 5px;
                }
        """
        self.setStyleSheet(self.buttonStyleAsText)
        self.setIconSize(self.muteIconPixmap.size())
        self.setIcon(self.muteIcon)
        self.clicked.connect(lambda: self.onButtonPressed())

    @Slot()
    def onButtonPressed(self):
        if self.semaphore:
            self.setIcon(self.muteIcon)
            self.semaphore = False
            self.parentPlayerWidget.currentPlayer.setMuted(True)
        else:
            self.setIcon(self.unmuteIcon)
            self.semaphore = True
            self.parentPlayerWidget.currentPlayer.setMuted(False)


    def setIconMuted(self):
        pass

    def setIconUnmuted(self):
        pass


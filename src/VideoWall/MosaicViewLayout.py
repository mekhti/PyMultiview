#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QGridLayout, QWidget
from PySide2.QtCore import QSize

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.SinglePlayer.SingleChannelLayout import SingleChannelLayout
from src.VideoWall.BlankWidget import BlankWidget
from src.VideoWall.GToolkit.GView import GView
from src.VideoWall.SP.SPLayout import SPLayout
from src.Models.PlayerBackend import PlayerBackend


class MosaicViewLayout(QGridLayout):
    objectID = None
    channelPlayers = list()
    horizontalCellCount = 2
    verticalCellCount = 2
    childLayoutWidth = 0
    childLayoutHeight = 0
    childWidgetSize = QSize(0, 0)

    def getObjectID(self):
        return self.objectID

    def __init__(self, pmConfig: PMConfig, parentDialogWindow: QWidget):
        """
        TODO: Implement parsing display configuration from config file
        """
        super(MosaicViewLayout, self).__init__()
        self.objectID = uuid4()
        self.pmConfig = pmConfig
        self.parentDialogWindow = parentDialogWindow
        self.parentDialogWidth = self.parentDialogWindow.width()
        self.parentDialogHeight = self.parentDialogWindow.height()
        self.__initUI__()

        for x in range(0, len(self.pmConfig.streams)):
            if self.pmConfig.appConfiguration.playerBackend == PlayerBackend.GTOOLKIT:
                self.channelPlayers.append(
                    GView(self.pmConfig, x, self.childWidgetSize)
                )
            elif self.pmConfig.appConfiguration.playerBackend == PlayerBackend.STANDART_PLAYER:
                self.channelPlayers.append(
                    SPLayout(self.childWidgetSize, self.pmConfig.streams[x])
                )

        self.currentIndex = 0
        for row in range(0, self.verticalCellCount):
            for col in range(0, self.horizontalCellCount):
                if self.currentIndex < len(self.channelPlayers):
                    if self.pmConfig.appConfiguration.playerBackend == PlayerBackend.GTOOLKIT:
                        self.addWidget(self.channelPlayers[self.currentIndex], row, col)
                    elif self.pmConfig.appConfiguration.playerBackend == PlayerBackend.STANDART_PLAYER:
                        self.addLayout(self.channelPlayers[self.currentIndex], row, col)

                    self.currentIndex += 1
                else:
                    self.addWidget(BlankWidget(self.childLayoutWidth, self.childLayoutHeight), row, col)

    def __setChildWidgetSize__(self) -> QSize:
        self.childLayoutWidth = int(self.parentDialogWidth / self.horizontalCellCount)
        self.childLayoutHeight = int(self.parentDialogHeight / self.verticalCellCount)
        self.childWidgetSize = QSize(int(self.parentDialogWidth / self.horizontalCellCount),
                                     int(self.parentDialogHeight / self.verticalCellCount))
        return self.childWidgetSize

    def __initUI__(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setHorizontalSpacing(0)
        self.setVerticalSpacing(0)
        self.__setChildWidgetSize__()

    def __initGUI__(self):
        pass

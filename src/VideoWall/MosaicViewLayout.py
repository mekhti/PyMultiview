#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QGridLayout, QWidget
from PySide2.QtCore import QSize

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.SinglePlayer.SingleChannelLayout import SingleChannelLayout
from src.VideoWall.BlankWidget import BlankWidget
from src.VideoWall.GToolkit.GView import GView


class MosaicViewLayout(QGridLayout):
    objectID = uuid4()
    useGToolkit = True
    channelPlayers = list()
    horizontalCellCount = 6
    verticalCellCount = 5
    childLayoutWidth = 0
    childLayoutHeight = 0
    childWidgetSize = QSize(0, 0)

    def __init__(self, pmConfig: PMConfig, parentDialogWindow: QWidget):
        """
        TODO: Implement parsing display configuration from config file
        """
        super(MosaicViewLayout, self).__init__()
        self.pmConfig = pmConfig
        self.parentDialogWindow = parentDialogWindow
        self.parentDialogWidth = self.parentDialogWindow.width()
        self.parentDialogHeight = self.parentDialogWindow.height()
        self.__initUI__()

        for x in range(0, len(self.pmConfig.streams)):
            print("Stream INDEX: ", x)
            if self.useGToolkit:
                self.channelPlayers.append(
                    GView(self.pmConfig, x, self.childWidgetSize)
                )
            else:
                self.channelPlayers.append(
                    SingleChannelLayout(self.pmConfig, x,
                                        self.childLayoutWidth,
                                        self.childLayoutHeight)
                )

        self.currentIndex = 0
        for row in range(0, self.verticalCellCount):
            for col in range(0, self.horizontalCellCount):
                if self.currentIndex < len(self.channelPlayers):
                    if self.useGToolkit:
                        self.addWidget(self.channelPlayers[self.currentIndex], row, col)
                    else:
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

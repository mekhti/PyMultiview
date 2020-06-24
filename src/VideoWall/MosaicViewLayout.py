#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QGridLayout, QDialog
from src.Controllers.PMConfig import PMConfig
from src.VideoWall.SinglePlayer.SingleChannelLayout import SingleChannelLayout
from src.VideoWall.BlankWidget import BlankWidget


class MosaicViewLayout(QGridLayout):
    channelPlayers = list()

    def __init__(self, pmConfig: PMConfig, parentDialogWindow: QDialog):
        super(MosaicViewLayout, self).__init__()
        self.pmConfig = pmConfig
        self.parentDialogWindow = parentDialogWindow
        self.setContentsMargins(0, 0, 0, 0)
        self.parentDialogWidth = self.parentDialogWindow.width()
        self.parentDialogHeight = self.parentDialogWindow.height()

        self.horizontalCellCount = 3
        self.verticalCellCount = 3

        self.childLayoutWidth = int(self.parentDialogWidth / self.horizontalCellCount)
        self.childLayoutHeight = int(self.parentDialogHeight / self.verticalCellCount)

        self.setHorizontalSpacing(0)
        self.setVerticalSpacing(0)

        for x in range(0, len(self.pmConfig.streams)):
            self.channelPlayers.append(
                SingleChannelLayout(self.pmConfig, x, self.childLayoutWidth, self.childLayoutHeight)
            )

        self.currentIndex = 0
        for row in range(0, self.verticalCellCount):
            for col in range(0, self.horizontalCellCount):
                if self.currentIndex < len(self.channelPlayers):
                    self.addLayout(self.channelPlayers[self.currentIndex], row, col)
                    self.currentIndex += 1
                else:
                    self.addWidget(BlankWidget(self.childLayoutWidth, self.childLayoutHeight), row, col)

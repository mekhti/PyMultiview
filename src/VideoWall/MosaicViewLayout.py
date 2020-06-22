#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QGridLayout, QDialog
from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget
from src.Controllers.PMConfig import PMConfig


class MosaicViewLayout(QGridLayout):
    playerWidgets = list()

    def __init__(self, pmConfig: PMConfig, parentDialogWindow: QDialog):
        super(MosaicViewLayout, self).__init__()
        self.pmConfig = pmConfig
        self.parentDialogWindow = parentDialogWindow

        self.setContentsMargins(0, 0, 0, 0)
        self.parentDialogWidth = self.parentDialogWindow.width()
        self.parentDialogHeight = self.parentDialogWindow.height()
        self.horisontalCellCount = 2
        self.verticalCellCount = 2
        #self.singlePlayerWidth = self.parentDialogWidth / pmConfig.displays[0]
        self.setHorizontalSpacing(0)
        self.setVerticalSpacing(0)
        self.setColumnMinimumWidth(self.horisontalCellCount, (self.parentDialogWidth / self.horisontalCellCount))
        self.setRowMinimumHeight(self.verticalCellCount, (self.parentDialogHeight / self.verticalCellCount))

        self.playerWidgets.append(SinglePlayerWidget(pmConfig, self.pmConfig.streams[0]))
        self.playerWidgets.append(SinglePlayerWidget(pmConfig, self.pmConfig.streams[1]))
        self.playerWidgets.append(SinglePlayerWidget(pmConfig, self.pmConfig.streams[2]))
        self.playerWidgets.append(SinglePlayerWidget(pmConfig, self.pmConfig.streams[3]))
        self.addWidget(self.playerWidgets[0], 0, 0)
        self.addWidget(self.playerWidgets[1], 0, 1)
        self.addWidget(self.playerWidgets[2], 1, 0)
        self.addWidget(self.playerWidgets[3], 1, 1)

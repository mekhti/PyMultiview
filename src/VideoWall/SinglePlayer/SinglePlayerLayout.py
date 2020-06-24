#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtWidgets, QtCore
from src.Controllers import PMConfig
from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget
from src.VideoWall.SinglePlayer.AudioWidget.AudioLayout import AudioLayout

# from src.Models.StreamConfiguration import StreamConfiguration


class SinglePlayerLayout(QtWidgets.QHBoxLayout):

    def __init__(self, pmConfig: PMConfig, streamIndex: int,
                 playerWidth: int, playerHeight: int ):
        super(SinglePlayerLayout, self).__init__()
        self.pmConfig = pmConfig
        self.playerWidth = playerWidth
        self.playerHeight = playerHeight
        self.setGeometry(QtCore.QRect(0, 0, self.playerWidth, self.playerHeight))
        self.setContentsMargins(0, 0, 0, 0)

        self.videoWidget = SinglePlayerWidget(pmConfig, self.pmConfig.streams[streamIndex],
                                              self.playerWidth, self.playerHeight)
        self.addWidget(self.videoWidget)

        self.audioLayout = AudioLayout()
        self.addLayout(self.audioLayout)


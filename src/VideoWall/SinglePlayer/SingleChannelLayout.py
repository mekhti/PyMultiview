#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QGridLayout
from PySide2.QtCore import QRect, Qt
from src.Controllers.PMConfig import PMConfig

from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget
from src.VideoWall.SinglePlayer.AudioWidget.AudioLayout import AudioLayout
from src.VideoWall.SinglePlayer.ChannelName import ChannelName


class SingleChannelLayout(QGridLayout):

    def __init__(self, pmConfig: PMConfig, streamIndex: int,
                 layoutWidth: int, layoutHeight: int):
        super(SingleChannelLayout, self).__init__()
        self.pmConfig = pmConfig
        self.streamIndex = streamIndex
        self.layoutWidth = layoutWidth
        self.layoutHeight = layoutHeight

        self.setContentsMargins(3, 3, 3, 3)
        self.setGeometry(QRect(0, 0, self.layoutWidth, self.layoutHeight))

        self.currentPlayerWidget = SinglePlayerWidget(self.pmConfig, self.pmConfig.streams[streamIndex],
                                                      self.layoutWidth, self.layoutHeight)
        self.addWidget(self.currentPlayerWidget, 0, 0)

        self.channelNameLabel = ChannelName(self.pmConfig.streams[streamIndex].sName)
        self.addWidget(self.channelNameLabel, 1, 0, Qt.AlignCenter)

        self.audioLayout = AudioLayout(self.currentPlayerWidget,
                                       int(self.layoutWidth * 0.05),
                                       self.layoutHeight)

        self.addLayout(self.audioLayout, 0, 1)


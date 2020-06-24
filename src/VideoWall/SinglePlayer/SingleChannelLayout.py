#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QVBoxLayout, QLabel
from PySide2.QtGui import QFont
from PySide2.QtCore import QRect
from src.Controllers.PMConfig import PMConfig
from src.VideoWall.SinglePlayer.SinglePlayerLayout import SinglePlayerLayout


class SingleChannelLayout(QVBoxLayout):

    def __init__(self, pmConfig: PMConfig, streamIndex: int,
                 layoutWidth: int, layoutHeight: int):
        super(SingleChannelLayout, self).__init__()
        self.pmConfig = pmConfig
        self.streamIndex = streamIndex
        self.layoutWidth = layoutWidth
        self.layoutHeight = layoutHeight

        self.setContentsMargins(1, 1, 1, 1)
        self.setGeometry(QRect(0, 0, self.layoutWidth, self.layoutHeight))

        self.currentPlayerlayout = SinglePlayerLayout(pmConfig,
                                                      self.streamIndex, self.layoutWidth,
                                                      self.layoutHeight - int(self.layoutHeight * 0.2))
        self.addLayout(self.currentPlayerlayout)

        self.videoName = QLabel(self.pmConfig.streams[streamIndex].sName)
        self.videoName.setFont(QFont("Arial", 14))
        self.addWidget(self.videoName)

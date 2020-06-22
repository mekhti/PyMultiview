#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtMultimediaWidgets
from src.VideoWall.SinglePlayer.StreamPlayer import StreamPlayer
from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.PMConfig import PMConfig


class SinglePlayerWidget(QtMultimediaWidgets.QVideoWidget):

    def __init__(self, pmConfig: PMConfig, streamConfiguration: StreamConfiguration): #, widgetWidth: int, widgetHeigth: int
        super(SinglePlayerWidget, self).__init__()
        self.pmConfig = pmConfig
        self.streamConfiguration = streamConfiguration
        #self.setMinimumWidth(widgetWidth)
        #self.setMinimumHeight(widgetHeigth)
        self.setMinimumWidth(200)
        self.setMinimumHeight(160)
        self.currentPlayer = StreamPlayer(self.streamConfiguration)
        self.currentPlayer.setVideoOutput(self)

    def __del__(self):
        if self.currentPlayer.isAvailable():
            self.currentPlayer.stop()



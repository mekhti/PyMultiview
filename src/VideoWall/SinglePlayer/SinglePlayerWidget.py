#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtMultimediaWidgets
from PySide2.QtWidgets import QLabel, QHBoxLayout
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPixmap, QPainter, QPaintEvent, QColor

from src.VideoWall.SinglePlayer.StreamPlayer import StreamPlayer
from src.Models.StreamConfiguration import StreamConfiguration
from src.Controllers.PMConfig import PMConfig


class SinglePlayerWidget(QtMultimediaWidgets.QVideoWidget):

    def __init__(self, pmConfig: PMConfig, streamConfiguration: StreamConfiguration,
                 widgetWidth: int, widgetHeigth: int):
        super(SinglePlayerWidget, self).__init__()
        self.pmConfig = pmConfig
        self.streamConfiguration = streamConfiguration
        self.widgetWidth = widgetWidth
        self.widgetHeight = widgetHeigth

        self.setMinimumWidth(widgetWidth)
        self.setMinimumHeight(widgetHeigth)
        self.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.currentPlayer = StreamPlayer(self.streamConfiguration)
        # self.currentPlayer.mediaStatusChanged(StreamPlayer.MediaStatus).connect(self.onMediaStatusChanged)

        self.noSignalPixmap = QPixmap("img/no-signal.jpg").scaled(self.widgetWidth,
                                                                  self.widgetHeight,
                                                                  Qt.IgnoreAspectRatio)

        self.noSignalPixmapLabel = QLabel()
        self.noSignalPixmapLabel.setPixmap(self.noSignalPixmap)
        self.noSignalLayout = QHBoxLayout()
        self.noSignalLayout.setContentsMargins(1, 1, 1, 1)
        self.noSignalLayout.addWidget(self.noSignalPixmapLabel)
        self.setLayout(self.noSignalLayout)

        self.currentPlayer.setVideoOutput(self)

    @Slot()
    def onMediaStatusChanged(self, currentStatus: StreamPlayer.MediaStatus):
        if currentStatus == StreamPlayer.UnknownMediaStatus \
                or currentStatus == StreamPlayer.NoMedia \
                or currentStatus == StreamPlayer.BufferingMedia:
            pass

    # TODO: Implement player stopping when window closed

    # def __del__(self):
    #     if self.currentPlayer.isAvailable():
    #         self.currentPlayer.stop()



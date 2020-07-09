#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtMultimediaWidgets import QGraphicsVideoItem
from PySide2.QtCore import QSizeF, Qt, Slot

from src.Controllers.PMConfig import PMConfig
from src.Models.StreamConfiguration import StreamConfiguration
from src.VideoWall.SinglePlayer.StreamPlayer import StreamPlayer


class ChannelPlayerWidget(QGraphicsVideoItem):

    def __init__(self, pmConfig: PMConfig, streamConfiguration: StreamConfiguration,
                 widgetWidth: int, widgetHeigth: int):
        super(ChannelPlayerWidget, self).__init__()
        self.pmConfig = pmConfig
        self.streamConfiguration = streamConfiguration
        self.widgetWidth = widgetWidth
        self.widgetHeight = widgetHeigth

        self.setSize(QSizeF(self.widgetWidth, self.widgetHeight))
        self.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)
        self.currentPlayer = StreamPlayer(self.streamConfiguration, parentWidget=self)
        self.scene().addWidget()


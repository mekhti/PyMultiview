#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtMultimediaWidgets import QGraphicsVideoItem
from PySide2.QtCore import QSize, Qt

from src.VideoWall.GToolkit.GPlayerV2 import GPlayerV2


class GVideoWidget(QGraphicsVideoItem):
    objectID = uuid4()

    def __init__(self, widgetSize: QSize, parent, inputStream):
        super(GVideoWidget, self).__init__()
        self.parentSceneItem = parent
        self.setSize(widgetSize)
        self.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.mainVideoPlayer = GPlayerV2(self, inputStream)
        self.mainVideoPlayer.setVideoOutput(self)

    def getPlayerObject(self):
        return self.mainVideoPlayer


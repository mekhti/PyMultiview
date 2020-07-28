#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtMultimediaWidgets import QGraphicsVideoItem
from PySide2.QtCore import QSize, Qt
from src.VideoWall.GToolkit.GPlayer import GPlayer


class GVideoWidget(QGraphicsVideoItem):
    objectID = None

    def __init__(self, widgetSize: QSize, parent, inputStream):
        super(GVideoWidget, self).__init__()
        self.objectID = uuid4()
        self.parentSceneItem = parent
        self.setSize(widgetSize)
        self.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.mainVideoPlayer = GPlayer(self, inputStream)
        self.mainVideoPlayer.setVideoOutput(self)

    def getPlayerObject(self):
        return self.mainVideoPlayer


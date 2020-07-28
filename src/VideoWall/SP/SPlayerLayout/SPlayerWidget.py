#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtCore import Qt, QSize
from PySide2.QtMultimediaWidgets import QVideoWidget
from src.Models.StreamConfiguration import StreamConfiguration
from src.VideoWall.SP.SPlayerLayout.SPlayer import SPlayer


class SPlayerWidget(QVideoWidget):
    """
    SPlayerWidget(parentSize: QSize, inputStream: StreamConfiguration)
    """
    objectID = uuid4()
    parentSize = None
    inputStream = None
    playerNode = None

    def __init__(self, parentSize: QSize, inputStream: StreamConfiguration):
        super(SPlayerWidget, self).__init__()
        self.parentSize = parentSize
        self.inputStream = inputStream

        self.setMinimumWidth(self.parentSize.width())
        self.setMinimumHeight(self.parentSize.height())
        self.setAspectRatioMode(Qt.AspectRatioMode.IgnoreAspectRatio)

        self.playerNode = SPlayer(self.inputStream)
        self.playerNode.setVideoOutput(self)

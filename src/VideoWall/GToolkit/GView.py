#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QGraphicsView
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QMouseEvent

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.GToolkit.GScene import GScene


class GView(QGraphicsView):
    objectID = uuid4()

    def __init__(self, pmConfig: PMConfig, streamIndex: int, widgetSize: QSize):
        super(GView, self).__init__()
        self.pmConfig = pmConfig
        self.streamIndex = streamIndex
        print("GView ID: ", self.objectID)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFixedSize(widgetSize)

        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(widgetSize)
        self.mainScene = GScene(widgetSize, self.pmConfig, self.streamIndex)
        self.setScene(self.mainScene)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        #TODO: Implement full screen video view on double click
        pass

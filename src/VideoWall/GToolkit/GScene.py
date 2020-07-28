#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtCore import QSize, Slot, Qt
from PySide2.QtGui import QPixmap

from src.Controllers.PMConfig import PMConfig
from src.VideoWall.GToolkit.GMuteButton import GMuteButton
from src.VideoWall.GToolkit.GVideoWidget import GVideoWidget
from src.VideoWall.SinglePlayer.ChannelName import ChannelName


class GScene(QGraphicsScene):
    objectID = None

    def __init__(self, widgetSize: QSize, pmConfig: PMConfig, streamIndex: int):
        super(GScene, self).__init__()
        self.objectID = uuid4()
        self.pmConfig = pmConfig
        self.widgetSize = widgetSize
        self.videoLostPixmap = QPixmap("img/no-signal.jpg").scaled(self.widgetSize,
                                                                   Qt.AspectRatioMode.IgnoreAspectRatio,
                                                                   Qt.TransformationMode.FastTransformation)
        self.setBackgroundBrush(self.videoLostPixmap)

        self.mainVideoItem = GVideoWidget(self.widgetSize, self, self.pmConfig.streams[streamIndex])
        self.addItem(self.mainVideoItem)

        self.muteButtonWidget = self.addWidget(GMuteButton(self.mainVideoItem.getPlayerObject()))
        self.muteButtonWidget.setPos(self.widgetSize.width() - self.muteButtonWidget.size().width() - 10, 10)

        channelNameLBL = ChannelName(self.pmConfig.streams[streamIndex].sName)
        self.channelNameLabel = self.addWidget(channelNameLBL)
        self.channelNameLabel.setX(int((self.widgetSize.width() - channelNameLBL.size().width()) / 2))
        self.channelNameLabel.setY(self.widgetSize.height() - channelNameLBL.size().height() - int(self.widgetSize.height() * 0.05))





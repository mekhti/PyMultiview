#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QVBoxLayout
from src.VideoWall.SinglePlayer.AudioWidget.MuteButton import MuteButton
from src.VideoWall.SinglePlayer.VuMeter.VuMeterWidget import VuMeterWidget

from src.VideoWall.SinglePlayer.SinglePlayerWidget import SinglePlayerWidget


class AudioLayout(QVBoxLayout):

    def __init__(self, parentPlayerWidget: SinglePlayerWidget,
                 widgetWidth: int, widgetHeight: int):
        super(AudioLayout, self).__init__()
        self.parentPlayerWidget = parentPlayerWidget
        self.widgetWidth = widgetWidth
        self.widgetHeight = widgetHeight

        self.muteUnmuteButton = MuteButton(self.parentPlayerWidget, self.widgetWidth, self.widgetWidth)
        self.addWidget(self.muteUnmuteButton)

        self.vuMeterWidget = VuMeterWidget(self.widgetWidth, self.widgetHeight)
        self.addWidget(self.vuMeterWidget)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QVBoxLayout
from src.VideoWall.SinglePlayer.AudioWidget.MuteButton import MuteButton
from src.VideoWall.SinglePlayer.VuMeter.VuMeterWidget import VuMeterWidget


class AudioLayout(QVBoxLayout):

    def __init__(self):
        super(AudioLayout, self).__init__()

        self.muteUnmuteButton = MuteButton()
        self.addWidget(self.muteUnmuteButton)

        self.vuMeterWidget = VuMeterWidget(50, 100)
        self.addWidget(self.vuMeterWidget)

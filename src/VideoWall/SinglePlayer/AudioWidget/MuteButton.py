#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QPushButton
from PySide2.QtGui import QPixmap, QIcon


class MuteButton(QPushButton):

    def __init__(self):
        super(MuteButton, self).__init__()

        self.setFixedSize(32, 32)

        self.muteIconPixmap = QPixmap("img/mute-red.png")
        self.muteIcon = QIcon(self.muteIconPixmap)

        self.unmuteIconPixmap = QPixmap("img/unmute-green.png")
        self.unmuteIcon = QIcon(self.unmuteIconPixmap)

        self.setIcon(self.muteIcon)




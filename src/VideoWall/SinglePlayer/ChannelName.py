#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


class ChannelName(QLabel):

    def __init__(self, channelName: str,
                 positionX: int = 0, positionY: int = 0,
                 labelWidth: int = 0, labelHeight: int = 0):
        super(ChannelName, self).__init__()
        self.setText(channelName)

        self.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        self.setContentsMargins(3, 3, 3, 3)
        self.styleAsText = """
        QLabel { 
            background-color : purple; 
            color : white;
            padding: 0px 2px 0px 2px; 
            }
        """
        self.setStyleSheet(self.styleAsText)
        self.setFont(QFont("Arial", 10, QFont.Bold))


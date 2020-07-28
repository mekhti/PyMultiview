#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtWidgets import QLabel
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


class SPChannelName(QLabel):
    """
    SPChannelName(channelName: str)
    """
    objectID = uuid4()

    def __init__(self, channelName: str):
        super(SPChannelName, self).__init__()
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


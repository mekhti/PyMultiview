#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from uuid import uuid4
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QWidget


class SPVUMeter(QWidget):
    """
    SPVUMeter(parentSize: QSize)
    """
    objectID = uuid4()
    parentSize = None
    
    def __init__(self, parentSize: QSize):
        super(SPVUMeter, self).__init__()

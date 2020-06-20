#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2 import QtGui, QtWidgets


class EditorWindow(QtGui.QWindow):

    def __init__(self):
        super(EditorWindow, self).__init__()
        self.setWidth(800)
        self.setHeight(600)
        self.setTitle("Edit configuration file")


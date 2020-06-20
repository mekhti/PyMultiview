# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from src.PyMultiview import PyMultiview


if __name__ == "__main__":
    app = QApplication([])
    window = PyMultiview()
    window.show()
    sys.exit(app.exec_())

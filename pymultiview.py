# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from src.PyMultiview import PyMultiview
from src.Controllers.PMConfig import PMConfig


if __name__ == "__main__":
    config = PMConfig()
    app = QApplication([])
    window = PyMultiview(config)
    window.show()
    sys.exit(app.exec_())

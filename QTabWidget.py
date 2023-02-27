import \
    sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTabWidget, )

import \
    ColorWidget as cw


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(800, 550))

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition(2))
        tabs.setTabShape(QTabWidget.TabShape(1))
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(cw.Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
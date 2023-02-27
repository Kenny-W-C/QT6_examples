import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, \
    QWidget

import ColorWidget as cw


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        x = 4400
        y = 200
        w = 2200
        h = 1100

        self.setWindowTitle("My App")
        self.setGeometry(x, y, w, h)

        layout = QGridLayout()
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(5)
        label = QLabel(self)
        pixmap = QPixmap('png\\2_of_clubs_scaled.png')
        # pixmap.scaledToHeight(75, mode = FastTransformation)
        label.setPixmap(pixmap)
        layout.addWidget(label, 0, 1)
        layout.addWidget(cw.Color('red'), 0, 3)
        layout.addWidget(cw.Color('cyan'), 0, 0)
        layout.addWidget(cw.Color('orange'), 2, 2)
        layout.addWidget(cw.Color('violet'), 3, 3)
        layout.addWidget(cw.Color('yellow'), 1, 1)
        layout.addWidget(cw.Color('blue'), 3, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

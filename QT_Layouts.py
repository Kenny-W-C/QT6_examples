import sys
import ColorWidget as cw
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, \
    QPushButton, \
    QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout1.setContentsMargins(15, 15, 15, 15)
        layout1.setSpacing(5)

        layout2.addWidget(cw.Color('red'))
        layout2.addWidget(cw.Color('yellow'))
        layout2.addWidget(cw.Color('purple'))
        layout1.addLayout(layout2)
        layout1.addWidget(cw.Color('green'))
        layout3.addWidget(cw.Color('red'))
        layout3.addWidget(cw.Color('purple'))
        layout1.addLayout(layout3)
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

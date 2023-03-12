import sys

from PyQt6.QtCore import QPointF, Qt
from PyQt6.QtGui import QBrush, QPainter, QPen, QPolygonF
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QPushButton,
    QSlider,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Defining a scene rect of 400x200, with it's origin at 0,0.
        # If we don't set this on creation, we can set it later with .setSceneRect
        self.scene = QGraphicsScene(0, 0, 400, 200)

        # Draw a rectangle item, setting the dimensions.
        rect = QGraphicsRectItem(0, 0, 200, 50)
        rect.setPos(50, 20)
        brush = QBrush(Qt.GlobalColor.red)
        rect.setBrush(brush)

        # Define the pen (line)
        pen = QPen(Qt.GlobalColor.cyan)
        pen.setWidth(10)
        rect.setPen(pen)

        ellipse = QGraphicsEllipseItem(0, 0, 100, 100)
        ellipse.setPos(75, 30)

        brush = QBrush(Qt.GlobalColor.blue)
        ellipse.setBrush(brush)

        pen = QPen(Qt.GlobalColor.green)
        pen.setWidth(5)
        ellipse.setPen(pen)

        textitem = self.scene.addText("QGraphics is fun!")
        textitem.setPos(100, 100)

        self.scene.addPolygon(
                QPolygonF(
                        [
                            QPointF(30, 60),
                            QPointF(270, 40),
                            QPointF(400, 200),
                            QPointF(20, 150),
                        ]),
                QPen(Qt.GlobalColor.darkGreen),
        )

        # Add the items to the scene. Items are stacked in the order they are added.
        self.scene.addItem(ellipse)
        self.scene.addItem(rect)

        # Set all items as movable and selectable.
        for item in self.scene.items():
            item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
            item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)

        # Define our layout.
        vbox = QVBoxLayout()

        up = QPushButton("Up")
        up.clicked.connect(self.up)
        vbox.addWidget(up)

        down = QPushButton("Down")
        down.clicked.connect(self.down)
        vbox.addWidget(down)

        rotate = QSlider()
        rotate.setRange(0, 360)
        rotate.valueChanged.connect(self.rotate)
        vbox.addWidget(rotate)

        view = QGraphicsView(self.scene)
        view.setRenderHint(QPainter.RenderHint.Antialiasing)

        hbox = QHBoxLayout(self)
        hbox.addLayout(vbox)
        hbox.addWidget(view)

        self.setLayout(hbox)

    def up(self):
        """ Iterate all selected items in the view, moving them forward. """
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z + 1)

    def down(self):
        """ Iterate all selected items in the view, moving them backward. """
        items = self.scene.selectedItems()
        for item in items:
            z = item.zValue()
            item.setZValue(z - 1)

    def rotate(self, value):
        """ Rotate the object by the received number of degrees. """
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(value)


app = QApplication(sys.argv)

w = Window()
w.show()

app.exec()

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def mapping(old_value, old_min, old_max, new_min, new_max):
    return (((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

class ColorWidget(QWidget):
    def __init__(self):
        super(ColorWidget, self).__init__()
        self.setupUi()
        self.currentCursorPosition = QPoint(0, 0)
        self.currentColor = QColor(255, 255, 255)

    def setupUi(self):
        self.setFixedSize(255, 255)
        self.setStyleSheet("background-color: #ffffff")

    def setCurrentPosition(self, newCurrentPosition):
        self.currentCursorPosition = newCurrentPosition
        self.updateColor()
        self.update()

    def updateColor(self):
        # Получаем цвет по текущей позиции курсора
        x = self.currentCursorPosition.x()
        y = self.currentCursorPosition.y()

        if 0 <= x < 255 and 0 <= y < 255:
            hue = mapping(x, 0, 255, 0, 360)
            saturation = mapping(y, 0, 255, 0, 255)
            self.currentColor = QColor.fromHsv(hue, saturation, 255)
            print(f"Selected Color: {self.currentColor.name()}")

    def mousePressEvent(self, event):
        self.setCurrentPosition(event.pos())

    def mouseMoveEvent(self, event):
        self.setCurrentPosition(event.pos())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # draw Background
        for x in range(256):
            for y in range(256):
                hue = mapping(x, 0, 255, 0, 360)
                saturation = mapping(y, 0, 255, 0, 255)
                color = QColor.fromHsv(hue, saturation, 255)
                painter.setPen(color)
                painter.drawPoint(x, y)

        # draw Cursor
        painter.setBrush(QColor(200, 200, 200))
        painter.drawEllipse(self.currentCursorPosition, 3, 3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ColorWidget()
    widget.show()
    sys.exit(app.exec_())

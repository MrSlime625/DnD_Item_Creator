from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os


class ItemImageWidget(QWidget):
    def __init__(self):
        super(ItemImageWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setFixedSize(450, 600)
        #self.setMinimumSize(QSize(300, 400))
        self.setStyleSheet("background-color: #ffffff")

        self.backgoundLabel = QLabel(self)
        self.backgoundLabel.setStyleSheet("background-color: none")
        self.backgoundLabel.setGeometry(QRect(0, 0, 450, 600))
        self.backgoundLabel.setText("")

        self.foregroundLabel = QLabel(self)
        self.foregroundLabel.setStyleSheet("background-color: none")
        self.foregroundLabel.setGeometry(QRect(0, 0, 450, 600))
        self.foregroundLabel.setText("")
        self.foregroundLabel.setPixmap(QPixmap("PresetPotion1.png"))
        self.foregroundLabel.setScaledContents(True)

        self.colorButton = QPushButton(self)
        self.colorButton.setText("Color")
        self.colorButton.setGeometry(QRect(10, 10, 60, 30))
        self.colorButton.clicked.connect(self.selectColor)

        self.saveButton = QPushButton(self)
        self.saveButton.setText("Save")
        self.saveButton.setGeometry(QRect(10, 40, 60, 30))
        self.saveButton.clicked.connect(self.take_screenshot)

        QMetaObject.connectSlotsByName(self)

        # self.points = []
        self.mainFillColor = QColor(100, 150, 200)

    def take_screenshot(self):
        # Создаем QImage с размерами виджета
        image = QImage(self.size(), QImage.Format_ARGB32)
        image.fill(Qt.white)  # Заполняем белым цветом

        # HideButtons
        self.colorButton.setHidden(True)
        self.saveButton.setHidden(True)

        # Создаем QPainter для отрисовки в QImage
        painter = QPainter(image)

        # Отрисовываем содержимое виджета в QImage
        self.render(painter)

        # Завершаем отрисовку
        painter.end()

        # Определяем имя файла для сохранения
        base_filename = "screenshot"
        extension = ".png"
        filename = base_filename + extension
        counter = 1

        # Проверяем, существует ли файл, и изменяем имя при необходимости
        while os.path.exists(filename):
            filename = f"{base_filename}{counter}{extension}"
            counter += 1

        # Сохраняем изображение в файл
        image.save(filename)

        # Show Buttons
        self.colorButton.setHidden(False)
        self.saveButton.setHidden(False)

    def paintEvent(self, event):
        # Создаем объект QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)


        # Устанавливаем цвет для рисования
        painter.setBrush(self.mainFillColor)
        painter.setPen(Qt.NoPen)

        points = [QPointF(112.6, 154.6), QPointF(122.6, 147.3), QPointF(128.0, 146.6), QPointF(141.3, 152.0),
                  QPointF(162.6, 156.6), QPointF(174.0, 156.0), QPointF(184.6, 154.0), QPointF(189.3, 157.3),
                  QPointF(197.3, 157.3), QPointF(206.0, 164.0), QPointF(206.0, 174.0), QPointF(202.0, 185.3),
                  QPointF(196.0, 201.3), QPointF(181.3, 229.3), QPointF(172.0, 249.3), QPointF(159.3, 280.6),
                  QPointF(144.0, 318.0), QPointF(130.6, 348.6), QPointF(122.6, 361.3), QPointF(111.3, 368.6),
                  QPointF(96.6, 370.6), QPointF(83.3, 368.6), QPointF(72.0, 365.3), QPointF(52.64, 351.3),
                  QPointF(44.64, 334.6), QPointF(46.0, 319.3), QPointF(55.36, 299.3), QPointF(62.0, 280.0),
                  QPointF(70.6, 262.0), QPointF(78.0, 246.6), QPointF(78.6, 237.3), QPointF(84.0, 231.3),
                  QPointF(96.0, 202.6), QPointF(109.3, 162.0)]

        for point in points:
            point.setX(point.x() * (3 / 2))
            point.setY(point.y() * (3 / 2))

        # if len(self.points) > 3:
        #     points.clear()
        #     for point in self.points:
        #         x = point.x() * 1.5
        #         y = point.y() * 1.5
        #         points.append(QPointF(x, y))

        painter.drawPolygon(points)
        self.update()

    # def mousePressEvent(self, event):
    #     # Получаем координаты клика
    #     x = event.x()
    #     y = event.y()
    #
    #     # Добавляем точку в список
    #     self.points.append(QPointF(x / 1.5, y / 1.5))
    #     print(self.points)

    def keyPressEvent(self, event):
        # Проверяем, нажата ли комбинация Ctrl + Z
        if event.key() == Qt.Key_Z and event.modifiers() == Qt.ControlModifier:
            try:
                self.points.pop()
            except:
                pass
        if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
            self.selectColor()
        if event.key() == Qt.Key_S and event.modifiers() == Qt.ControlModifier:
            self.take_screenshot()

    def selectColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.mainFillColor = QColor(color.rgb())

    def resizeEvent(self, event):
        # Игнорируем событие изменения размера
        event.ignore()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    widget = ItemImageWidget()
    widget.show()
    sys.exit(app.exec_())

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from DnDDataViewerWidget import DnDDataViewerWidget
from DnDItemPropertyEditor import DnDItemPropertyEditor


class DnDItemCreator(QMainWindow):
    def __init__(self, *args):
        super(DnDItemCreator, self).__init__(*args)
        self.setupUI()
        self.initTriggers()

    def setupUI(self):
        self.setStyleSheet("""
QWidget {
    border: 1px solid #303038;
    border-radius: 5px;
    color: #d4ffff;
    background-color: #484848;
    font: 75 14pt \"Arial\";
}

QPushButton {
    border: 1px solid #303038;
    border-radius: 5px;
    width: 80px;
    height: 30px;
    color: #cccccc;
}
QPushButton:hover {
    background-color: #707070;
}
QPushButton:pressed {
    background-color: #505060;     
}

QFrame {border: 1px solid #303038}

QLabel {border: none; color: #cccccc;}

QSpinBox::up-button {
    background-color: none; /* Цвет фона кнопки увеличения */
    border: none; /* Цвет рамки кнопки увеличения */
    border-radius: 5px; /* Радиус закругления углов кнопки увеличения */
    margin-right: 2px;
    image: url(Images/up-arrow.png);
}

QSpinBox::up-button:hover {
    background-color: #606060; /* Цвет фона кнопки увеличения при наведении */
}

QSpinBox::up-button:pressed {
    background-color: #6060f0; /* Цвет фона кнопки увеличения при нажатии */
}

QSpinBox::down-button {
    background-color: none; /* Цвет фона кнопки увеличения */
    border: none; /* Цвет рамки кнопки увеличения */
    border-radius: 5px; /* Радиус закругления углов кнопки увеличения */
    margin-right: 2px;
    image: url(Images/down-arrow.png);
}

QSpinBox::down-button:hover {
    background-color: #606060; /* Цвет фона кнопки увеличения при наведении */
}

QSpinBox::down-button:pressed {
    background-color: #6060f0; /* Цвет фона кнопки увеличения при нажатии */
}

QDoubleSpinBox::up-button {
    background-color: none; /* Цвет фона кнопки увеличения */
    border: none; /* Цвет рамки кнопки увеличения */
    border-radius: 5px; /* Радиус закругления углов кнопки увеличения */
    margin-right: 2px;
    image: url(Images/up-arrow.png);
}

QDoubleSpinBox::up-button:hover {
    background-color: #606060; /* Цвет фона кнопки увеличения при наведении */
}

QDoubleSpinBox::up-button:pressed {
    background-color: #6060f0; /* Цвет фона кнопки увеличения при нажатии */
}

QDoubleSpinBox::down-button {
    background-color: none; /* Цвет фона кнопки увеличения */
    border: none; /* Цвет рамки кнопки увеличения */
    border-radius: 5px; /* Радиус закругления углов кнопки увеличения */
    margin-right: 2px;
    image: url(Images/down-arrow.png);
}

QDoubleSpinBox::down-button:hover {
    background-color: #606060; /* Цвет фона кнопки увеличения при наведении */
}

QDoubleSpinBox::down-button:pressed {
    background-color: #6060f0; /* Цвет фона кнопки увеличения при нажатии */
}

QComboBox::drop-down {
    background-color: none; /* Цвет фона кнопки раскрытия */
    border: none; /* Цвет рамки кнопки раскрытия */
    border-radius: 5px; /* Радиус закругления углов кнопки раскрытия */
    image: url(Images/down-arrow.png); /* Путь к изображению стрелочки вниз */
    margin-right: 2px;
    margin-top: 4px;
    width: 18px; /* Ширина кнопки раскрытия */
    height: 18px; /* Высота кнопки раскрытия */
}
QComboBox::drop-down:hover {
    background-color: #606060; /* Цвет фона кнопки раскрытия при наведении */
}

QComboBox::drop-down:pressed {
    background-color: #6060f0; /* Цвет фона кнопки раскрытия при нажатии */
}

QLineEdit {
    background-color: #424248; /* Цвет фона таблицы */
}
QPlainTextEdit {
    background-color: #424248; /* Цвет фона таблицы */
}

QTableWidget {
    background-color: #424248; /* Цвет фона таблицы */
}

QTableWidget::item:selected {
    background-color: #606075; /* Цвет фона выделенной ячейки */
    color: #f4ffff; /* Цвет текста выделенной ячейки */
}

QHeaderView::section {
    background-color: #303038; /* Цвет фона заголовков */
    color: #cccccc; /* Цвет текста заголовков */
    padding: 5px; /* Внутренний отступ для заголовков */
    border: none; /* Цвет рамки заголовков */
    font-weight: bold; /* Жирный шрифт для заголовков */
}

QHeaderView::corner {
    background-color: #303038; /* Цвет фона углового заголовка */
    border: none; /* Убираем рамку */
}
""")

        self.centralWidget = QWidget(self)
        self.mainLayout = QHBoxLayout(self)

        self.dataViewer = DnDDataViewerWidget()
        self.propertyEditor = DnDItemPropertyEditor()
        self.verticalLine = QFrame(self)

        self.verticalLine.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding))
        self.verticalLine.setFrameShape(QFrame.VLine)
        self.verticalLine.setFrameShadow(QFrame.Sunken)

        self.mainLayout.addWidget(self.dataViewer)
        self.mainLayout.addWidget(self.verticalLine)
        self.mainLayout.addWidget(self.propertyEditor)

        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

    def initTriggers(self):
        pass


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = DnDItemCreator()
    window.showMaximized()
    sys.exit(app.exec_())

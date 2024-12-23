from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog
import json

class DnDDataViewerWidget(QWidget):
    def __init__(self):
        super(DnDDataViewerWidget, self).__init__()
        self.setupUi(self)
        self.initTriggers()

    def setupUi(self, DnDDataViewerWidget):
        DnDDataViewerWidget.setObjectName("DnDDataViewerWidget")
        DnDDataViewerWidget.resize(200, 750)
        DnDDataViewerWidget.setMinimumSize(QtCore.QSize(200, 750))
        DnDDataViewerWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(DnDDataViewerWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dataLabel = QtWidgets.QLabel(DnDDataViewerWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")
        self.horizontalLayout.addWidget(self.dataLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.openButton = QtWidgets.QPushButton(DnDDataViewerWidget)
        self.openButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.openButton.setFont(font)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(DnDDataViewerWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(DnDDataViewerWidget)
        QtCore.QMetaObject.connectSlotsByName(DnDDataViewerWidget)

    def retranslateUi(self, DnDDataViewerWidget):
        _translate = QtCore.QCoreApplication.translate
        DnDDataViewerWidget.setWindowTitle(_translate("DnDDataViewerWidget", "Form"))
        self.dataLabel.setText(_translate("DnDDataViewerWidget", "NoSelectJson"))
        self.openButton.setText(_translate("DnDDataViewerWidget", "Open"))

    def initTriggers(self):
        self.openButton.clicked.connect(self.handlerListWidget)

    def handlerListWidget(self):
        path = self.openFileDialog()
        if path:
            dataJson = None
            with open(path, "r", encoding="utf-8") as fileJson:
                dataJson = json.loads(fileJson.read())
                fileJson.close()
        for item in dataJson["Items"]:
            self.listWidget.addItem(item)

    def openFileDialog(self, parent=None):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly  # Устанавливаем режим только для чтения
        file_path, _ = QFileDialog.getOpenFileName(parent, "Выберите файл", "",
                                                   "Все файлы (*);;Изображения (*.png)", options=options)

        return file_path if file_path else None

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = DnDDataViewerWidget()
    widget.show()
    sys.exit(app.exec_())

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *

from DnDComboBoxDice import DnDComboBoxDice
import json


class DnDTableWidgetStatsItem(QTableWidget):
    def __init__(self):
        super(DnDTableWidgetStatsItem, self).__init__()
        self.setupUI()
        self.initTriggers()
        self.pathToPresetsStats = r"Jsons/PresetsStats.json"

    def setupUI(self):

        self.setColumnCount(6)
        self.setRowCount(3)
        self.horizontalHeader().setStretchLastSection(True)

        for column in [0, 2, 4]:
            self.setColumnWidth(column, 200)

        for column in [1, 3, 5]:
            self.horizontalHeader().setSectionResizeMode(column, QHeaderView.Stretch)

        self.setHorizontalHeaderItem(0, QTableWidgetItem("Property"))
        self.setHorizontalHeaderItem(2, QTableWidgetItem("Property"))
        self.setHorizontalHeaderItem(4, QTableWidgetItem("Property"))

        self.setHorizontalHeaderItem(1, QTableWidgetItem("Value"))
        self.setHorizontalHeaderItem(3, QTableWidgetItem("Value"))
        self.setHorizontalHeaderItem(5, QTableWidgetItem("Value"))

        self.setStats()

    def setStats(self, typeItem="Weapons", customType=""):
        self.setRowCount(0)

        if typeItem != "Custom Type":
            dataJson = None
            with open(r"Jsons/PresetsStats.json", "r", encoding="utf-8") as presetStatsFile:
                dataJson = json.loads(presetStatsFile.read())
                presetStatsFile.close()

            self.setRowCount(len(dataJson[typeItem]) // 3 + 1)

            indexHorizontal = 0
            indexVertical = 0

            for propertyFromJson in dataJson[typeItem]:

                propertyName = propertyFromJson
                propertyType = dataJson[typeItem][propertyFromJson]["type"]
                propertyValue = dataJson[typeItem][propertyFromJson]["value"]

                self.addProperty(indexHorizontal, indexVertical, propertyName)
                if propertyType == "Int":
                    self.addValueInt(indexHorizontal + 1, indexVertical, propertyValue)

                elif propertyType == "Float":
                    self.addValueFloat(indexHorizontal + 1, indexVertical, propertyValue)

                elif propertyType == "Dice":
                    self.addValueDice(indexHorizontal + 1, indexVertical, propertyValue[0], propertyValue[1])

                elif propertyType == "ComboBox":
                    self.addValueComboBox(indexHorizontal + 1, indexVertical, propertyValue)

                elif propertyType == "String":
                    self.addValueString(indexHorizontal + 1, indexVertical, propertyValue)

                indexHorizontal += 2

                if indexHorizontal == 6:
                    indexHorizontal = 0
                    indexVertical += 1

        elif typeItem == "Custom Type":
            self.setRowCount(3)

    def addRowBottom(self):
        self.setRowCount(self.rowCount() + 1)

    def addValueString(self, x, y, startValue="None"):
        if startValue == "":
            startValue = "None"
        item = QTableWidgetItem(startValue)
        self.setItem(y, x, item)

    def addValueDice(self, x, y, startValue=1, startDice=1):
        widget = QWidget()
        comboBox = DnDComboBoxDice()
        spinBox = QSpinBox()
        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        spinBox.setValue(startValue)
        spinBox.setMaximum(1000000000)
        comboBox.setCurrentIndex(startDice)

        layout.addWidget(spinBox)
        layout.addWidget(comboBox)

        widget.setLayout(layout)

        self.setCellWidget(y, x, widget)

    def addValueInt(self, x, y, startValue=1):
        spinBox = QSpinBox()
        spinBox.setValue(startValue)
        spinBox.setMaximum(1000000000)
        self.setCellWidget(y, x, spinBox)

    def addValueFloat(self, x, y, startValue=1):
        spinBox = QDoubleSpinBox()
        spinBox.setValue(startValue)
        spinBox.setMaximum(1000000000)
        self.setCellWidget(y, x, spinBox)

    def addValueComboBox(self, x, y, listValues):
        comboBox = QComboBox()
        comboBox.addItems(listValues)
        self.setCellWidget(y, x, comboBox)

    def addProperty(self, x, y, propertyName="None Property"):
        item = QTableWidgetItem(propertyName)
        item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.setItem(y, x, item)

    def initTriggers(self):
        pass

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DnDComboBoxDice(QComboBox):
    def __init__(self):
        super(DnDComboBoxDice, self).__init__()
        self.addItems(["d4", "d6", "d8", "d10", "d12", "d20", "d100"])

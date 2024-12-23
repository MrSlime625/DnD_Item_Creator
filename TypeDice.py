import dataclasses


@dataclasses.dataclass
class TypeDice:
    valueCount: int = 0
    valueType: int = 0

    # Table Value Type:
    # 0 - d4
    # 1 - d6
    # 2 - d8
    # 3 - d10
    # 4 - d12
    # 5 - d20
    # 6 - d100

    def __init__(self, startCount, startType):
        self.valueCount = startCount
        self.valueType = startType

    def setCount(self, newCount):
        self.valueCount = newCount

    def setType(self, newType):
        self.valueType = newType

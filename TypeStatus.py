import dataclasses


@dataclasses.dataclass
class TypeStatus:
    value: str = "New"
    listAllTypes: tuple = ("New", "Damaged", "Broken")

    def __init__(self, startValue):
        self.value = startValue

    def setValue(self, newValue: str):
        self.value = newValue

import dataclasses


@dataclasses.dataclass
class TypeMaterialWeapons:
    value: str = "Steel"
    listAllTypes: tuple = ("Wood", "Iron", "Steel")

    def __init__(self, startValue):
        self.value = startValue

    def setValue(self, newValue: str):
        self.value = newValue

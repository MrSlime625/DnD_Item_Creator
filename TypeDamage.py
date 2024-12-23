import dataclasses


@dataclasses.dataclass
class TypeDamage:
    value: str = "Splash"
    listAllTypes: tuple = ("", "", "")

    def __init__(self, startValue):
        self.value = startValue

    def setValue(self, newValue: str):
        self.value = newValue

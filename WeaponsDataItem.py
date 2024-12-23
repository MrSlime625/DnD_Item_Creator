import dataclasses
from TypeDice import TypeDice
from TypeDamage import TypeDamage
from TypeMaterialWeapons import TypeMaterialWeapons
from TypeStatus import TypeStatus


@dataclasses.dataclass
class WeaponsItemData:
    _weight: float = 1
    _damage: TypeDice = TypeDice(1, 0)
    _longRange: float = 1.5
    _damageType: TypeDamage = TypeDamage("Splash")
    _beauty: int = 50
    _material: TypeMaterialWeapons = TypeMaterialWeapons("Steel")
    _proficiencyClass: int = 1
    _price: int = 1
    _attackSpeed: float = 1.2
    _dropdown: int = 0
    _changed: int = -1
    _levelDependence: int = 1
    _status: TypeStatus = TypeStatus("New")

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, value: float):
        self._weight = value

    @property
    def damage(self) -> TypeDice:
        return self._damage

    @damage.setter
    def damage(self, value: TypeDice):
        self._damage = value

    @property
    def longRange(self) -> float:
        return self._longRange

    @longRange.setter
    def longRange(self, value: float):
        self._longRange = value

    @property
    def damageType(self) -> TypeDamage:
        return self._damageType

    @damageType.setter
    def damageType(self, value: TypeDamage):
        self._damageType = value

    @property
    def beauty(self) -> int:
        return self._beauty

    @beauty.setter
    def beauty(self, value: int):
        self._beauty = value

    @property
    def material(self) -> TypeMaterialWeapons:
        return self._material

    @material.setter
    def material(self, value: TypeMaterialWeapons):
        self._material = value

    @property
    def proffesionalClass(self) -> int:
        return self._proficiencyClass

    @proffesionalClass.setter
    def proffesionalClass(self, value: int):
        self._proficiencyClass = value

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int):
        self._price = value

    @property
    def attackSpeed(self) -> float:
        return self._attackSpeed

    @attackSpeed.setter
    def attackSpeed(self, value: float):
        self._attackSpeed = value

    @property
    def dropdown(self) -> int:
        return self._dropdown

    @dropdown.setter
    def dropdown(self, value: int):
        self._dropdown = value

    @property
    def changed(self) -> int:
        return self._changed

    @changed.setter
    def changed(self, value: int):
        self._changed = value

    @property
    def levelDependence(self) -> int:
        return self._levelDependence

    @levelDependence.setter
    def levelDependence(self, value: int):
        self._levelDependence = value

    @property
    def status(self) -> TypeStatus:
        return self._status

    @status.setter
    def status(self, value: TypeStatus):
        self._status = value

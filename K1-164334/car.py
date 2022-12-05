import vehicle from vehicle

class Car:
    is_combi: bool


    def __init__(self, brand: str, model: int, price: float, min_speed: int, weight: int, is_combi: bool) -> None:
        self._brand = brand

        self._model = model
        if self._model < 0:
            self._model = 0
        else:
            return self._model

        self._price = price
        if self._price < 0:
            self._price = 0
        else:
            return self._price

        self._min_speed = min_speed
        if self._min_speed < 50:
            self._min_speed = 50
        else:
            return self._min_speed

        self._weight = weight
        if self._weight < 0:
            self._weight = 0
        else:
            return self._weigh

        self._is_combi = is_combi

        @property
        def brand(self) -> str:
            return self._brand

        @brand.setter
        def brand(self, brand: str) -> str:
            if self._brand != str:
                print()
            else:
                return self._brand

        @property
        def model(self) -> int:
            return self._model

        @model.setter
        def model(self, model: int) -> int:
            self._model = model
            if self._model < 0:
                self._model = 0
            else:
                return self._model

        @property
        def price(self) -> float:
            return self._price

        @price.setter
        def price(self, price: float) -> float:
            self._price = price
            if self._price < 0:
                self._price = 0
            else:
                return self._price

        @property
        def min_speed(self) -> int:
            return self._min_speed

        @min_speed.setter
        def min_speed(self, min_speed: int) -> int:
            self._min_speed = min_speed
            if self._min_speed < 50:
                self._min_speed = 50
            else:
                return self._min_speed

        @property
        def weight(self) -> int:
            return self._weight

        @weight.setter
        def weight(self, weight: int) -> int:
            self._weight = weight
            if self._weight < 0:
                self._weight = 0
            else:
                return self._weight

        @property
        def _is_combi(self) -> bool:
            return self._is_combi

        @is_combi.setter
        def is_combi(self, is_combi: bool) -> bool:
            if self._is_combi != bool:
                print()
            else:
                return self._is_combi
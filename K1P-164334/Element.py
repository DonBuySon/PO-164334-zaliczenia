class Element:
    __name: str
    __year: int

    def __init__(self, name: str = None, year: int = 1970) -> None:
            self.__name = name
            self.__year = year
            if year > 2023 and year < 1970:
                year = 1970

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int) -> None:
        self.__year = year
        if year > 2023 and year <1970:
            year = 1970

    def __repr__(self):
        return "Nazwa:\n" + str(self.name) + ". Utworzony\n" + int(self.year)

from Element import Element

class File(Element):
    __size: int

    def __init__ (self, name: str, year: int, size: int = 0) -> None:
        self.__name = name
        self.__year = year
        if year > 2023 and year < 1970:
            year = 1970
        self.__size = size
        if size < 0:
            size = 0

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

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        self.__size = size
        if size < 0:
            size = 0

    def __repr__(self):
        return "Nazwa:\n" + str(self.name) + ". Utworzony\n" + int(self.year) + ". Rozmiar\n" + int(self.size)

class Directory(Element):
    __elements: list[File]

    def __init__ (self, name: str, year: int, elements: list[File]) -> None:
        self.__name = name
        self.__year = year
        if year > 2023 and year < 1970:
            year = 1970
        self.__elements = elements

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

    @property
    def elements(self) -> list[File]:
        return self.__elements

    @elements.setter
    def elements(self, elements: list[File]) -> None:
        self.__elements = elements

from Element import Element
from File import File

def main():
    e1 = Element("element1", 1998)
    print(e1)

    e2 = Element("element1", 1960)
    print(e2)

    print(e1 != e2)
    print(e1 == e2)

    e2.year = 1998

    print(e2)

    print(e1 != e2)
    print(e1 == e2)

    e3 = File("element2", 1998, 997)
    print(e3)

    e4 = File("element2", 1960, 124)
    print(e4)

    print(e3 != e4)
    print(e3 == e4)

    e4.year = 1998
    e4.size = 997

    print(e4)

    print(e3 != e4)
    print(e3 == e4)
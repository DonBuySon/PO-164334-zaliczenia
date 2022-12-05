import car from car
import vehicle from vehicle

def __main__():
    v_1 = Vehicle("Ferrari", 7, 4300, 1000500100900, 1000)
    v_2 = Vehicle("Fiat", 126, 1000000000, 15, 800)

    c_1 = Car("Warszawa", 1, 123987, 2, 12345679, "tak")
    c_2 = Car("Aston Martin", 7, 4300, 1000500100900, 1000, "nie")

    print(v_1, v_2, c_1, c_2)
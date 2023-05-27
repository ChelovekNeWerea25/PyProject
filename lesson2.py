class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passenger(self):
        if self.passengers:
            print(f"\nВ машині {self.brand} є такі пасажири:", end=" ")
            for passenger in self.passengers:
                print(passenger.name, end=" ")
        else:
            print(f"\nВ машині {self.brand} нікого немає")


h1 = Human("Женя")
h2 = Human("Сергей")
h3 = Human("Ярік")
car1 = Auto("Абобус")
car2 = Auto("Тесла")
car3 = Auto("Ауді")
car1.add_passenger(h1, h2, h3)
car2.add_passenger(h1, h3)
car1.print_passenger()
car2.print_passenger()
car3.print_passenger()

class Human:
    def __init__(self, name):
        self.name = name


class Auto:
    def __init__(self, brand, color, number):
        self.brand = brand
        self.color = color
        self.number = number
        self.passengers = []

    def add_passenger(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passenger(self):
        if self.passengers:
            print(f"\nВ машині {self.brand} з гос номером '{self.number}' колір якої '{self.color}' є такі пасажири:",
                  end=" ")
            for passenger in self.passengers:
                print(passenger.name, end=" ")
        else:
            print(f"\nВ машині {self.brand} з гос номером '{self.number}' колір якої '{self.color}' нікого немає")


h1 = Human("Женя")
h2 = Human("Сергей")
h3 = Human("Ярік")
car1 = Auto("Абобус", "Жовтий", "BI3587AG")
car2 = Auto("Тесла", "Білий", "BI4576YY")
car3 = Auto("Ауді", "Чорний", "BI7587CH")
car1.add_passenger(h1, h2, h3)
car2.add_passenger(h1, h3)
car1.print_passenger()
car2.print_passenger()
car3.print_passenger()

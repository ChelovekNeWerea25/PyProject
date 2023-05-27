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
        if(self.passengers):
            print(f"В машині {self.brand} є такі пасажири:")
            for passenger in self.passengers:
                print(passenger.name)

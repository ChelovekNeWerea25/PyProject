import os


class week:
    def __init__(self, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):
        self.monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday
        self.__Saturday = Saturday
        self.Sunday = Sunday

    def set_saturday(self, dilo):
        self.__Saturday = dilo

    def get_saturday(self):
        return self.__Saturday

    def printing(self):
        print("Діло в Monday:", self.monday)
        print("Діло в Tuesday:", self.Tuesday)
        print("Діло в Wednesday:", self.Wednesday)
        print("Діло в Thursday:", self.Thursday)
        print("Діло в Friday:", self.Friday)


h1 = week("Спать", "Спать", "Спать", "Спать", "Спать", "Спать?", "Спать")
h1.printing()
h1.set_saturday("Идти в академию")
print("Діло в Saturday:", h1.get_saturday())
print("Діло в Sunday:", h1.Sunday)

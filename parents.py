class grddad:
    def __init__(self, age, name, surname):
        self.age = age
        self.name = name
        self.surname = surname
        self.printing()

    def printing(self):
        print(f"Дід: Очі = {self.eye} Вік = {self.age} Ім'я = {self.name} Фамілія = {self.surname}")

    eye = "Карі"


class dad(grddad):
    secondname = "Горбунов"

    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.printing()

    def printing(self):
        print(f"Тато: Очі = {self.eye} Вік = {self.age} Ім'я = {self.name} Фамілія = {self.secondname}")


class son(dad):
    def __init__(self, age, name, hobby):
        self.age = age
        self.name = name
        self.hobby = hobby
        self.printing()

    def printing(self):
        print(f"Син: Очі = {self.eye} Вік = {self.age} Ім'я = {self.name} Фамілія = {dad.secondname}")


h2 = grddad(83, "Fedko", "Koval")
h3 = dad(37, "Vana")
h1 = son(9, "Anton", "sport")

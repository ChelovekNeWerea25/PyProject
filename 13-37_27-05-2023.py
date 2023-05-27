class Human:
    day = "Sybota"


class Student(Human):
    def __init__(self, dz, raiting):
        self.dz = dz
        self.raiting = raiting

    def print_student(self):
        print(f"В учня {self.dz} просрочок та {self.raiting} місце в рейтингу")


class Dima(Student):
    def __init__(self, hobby):
        self.hobby = hobby

    def printing(self):
        print(f"Зохоплення студента це {self.hobby}")


class Zenya(Human):
    def __init__(self, group, mark):
        self.group = group
        self.mark = mark

    def prntzenya(self):
        print(f"Вчитель веде групу {self.group} і поставив середню оцінку {self.mark}")

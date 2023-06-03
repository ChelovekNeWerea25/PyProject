class duck:
    def sound(self):
        print("Kra")


class Human:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print('Robit dz')


a1 = duck()
h = Human("Ivan")
a1.sound()
h.sound()

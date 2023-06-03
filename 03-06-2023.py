class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age


h = Human("Jena", 23)
print(h.name)

class car:
    def __init__(self, marka, engine):
        self.marka = marka
        self.__engine = engine

    def printing(self):
        print(f"Марка машини {self.marka} в неї {self.__engine}л об'єм двигуна")


h = car("BMW", 23)
print(h.marka)
print(h._car__engine)
h.printing()

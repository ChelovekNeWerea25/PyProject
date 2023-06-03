class car:
    def __init__(self, marka, engine):
        self.marka = marka
        self.__engine = engine

    def printing(self):
        print(f"Марка машини {self.marka} в неї {self.__engine}л об'єм двигуна")

    def get_engine(self):
        return self.__engine


h = car("BMW", 23)
print(h.marka, h.get_engine())
h.printing()

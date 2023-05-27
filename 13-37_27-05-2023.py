class Human:
    day="Sybota"
    def __init__(self,dz,raiting):
        self.dz=dz
        self.raiting=raiting
    def print_student(self):
        print(f"В учня {self.dz} просрочок та {self.raiting} місце в рейтингу")

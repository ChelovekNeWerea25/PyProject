class Student:
    def __init__(self,name):
        self.name=name
        self.radist=1
        self.life=True
        self.pregress=1
    def study(self):
        print("📚ЧАС ДЛЯ НАВЧАННЯ📚")
        self.radist-=0.5
        self.pregress+=1
    def chill(self):
        print("🎮ЧАС ДЛЯ ДЕГРАДАЦІЇ🎮")
        self.radist+=1
        self.pregress-=0.5
    def sleep(self):
        print("☁ЧАС ДЛЯ СНУ☁")
        self.radist+=1

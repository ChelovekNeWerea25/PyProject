from time import sleep


class Student:
    def __init__(self):
        self.name=input("Введіть ім'я вашого персонажу:")
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
    def russia(self):
        print("🧳ЧАС ДЛЯ ПОДОРОЖІ В росію🧳")
        self.radist=0
        self.pregress=0
        self.life=False
        sleep(2)
        print(f"{self.name} помер від крінжа")

    def check(self):
        if self.radist <=0:
            print(f'{self.name} помер від депресії')
            self.life = False
        elif self.pregress<=0:
            print(f"{self.name} помер, бо стали тупими!")
            self.life=False
    def dayoff(self):
        print(f"У {self.name} радість = {self.radist},а прогресс {self.pregress}")
human=Student()
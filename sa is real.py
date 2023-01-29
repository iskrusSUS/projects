import random

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.work = 0
        self.money = 0

    def to_study(self):
        print('Time to study!')
        self.progress += 0.15
        self.gladness -= 3
        self.work = 0

    def to_sleep(self):
        print('I will sleep..')
        self.gladness += 3
        self.work = 0

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.2
        self.money -= 50
        self.work = 0

    def to_work(self):
        print('Time to work!')
        self.money += 40
        self.gladness -= 3
        self.work += 1

    def is_alive(self):
        if self.progress < -0.5:
            print('cast out....')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression..')
            self.alive = False
        elif self.progress > 5:
            print ('passed externally....')
            self.alive = False

    def end_of_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
        print(f'Money = {self.money}')

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")

        if self.money < 50:
            self.to_work()
        elif self.work < 5:
            self.to_study()
        else:
            live_cube = random.randint(1, 3)
            if live_cube == 1:
                self.to_study()
            elif live_cube == 2:
                self.to_sleep()
            elif live_cube == 3:
                self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name='Nick')

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.hunger = 0
        self.alive = True

    def eat(self):
        print('Time to eat!')
        self.hunger -= 3
        self.happiness += 2

    def sleep(self):
        print('Time for a nap...')
        self.happiness += 3
        self.hunger += 1

    def play(self):
        print('Time to play!')
        self.happiness += 5
        self.hunger += 2

    def check_status(self):
        if self.hunger > 10:
            print('Starving...')
            self.alive = False
        elif self.happiness <= 0:
            print('Depression..')
        self.alive = False

def end_of_day(self):
    print(f'Hunger = {self.hunger}')
    print(f'Happiness = {self.happiness}')

def live(self, day):
    day = "Day " + str(day) + " of " + self.name + "'s life"
    print(f"{day:=^50}")
    action = random.randint(1, 3)
    if action == 1:
        self.eat()
    elif action == 2:
        self.sleep()
    elif action == 3:
        self.play()
    self.end_of_day()
    self.check_status()

fluffy = Cat(name='Fluffy')
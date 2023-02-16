import random


class Cat:
    def __init__(self, name='Cat', home=None, breed=None):
        self.name = name
        self.home = home
        self.breed = breed
        self.happiness = 50
        self.hunger = 50
        self.money = 100

    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.hunger > 100:
                self.hunger = 100
                return
            self.hunger += 5
            self.home.food -= 5

    def sleep(self):
        self.happiness += 10
        self.home.mess += 5

    def play(self):
        self.happiness += 10
        self.hunger -= 5

    def shopping(self, manage):
        if manage == 'food':
            print('Bought food')
            self.money -= 50
            self.home.food += 50
        else:
            return

    def to_repair(self):
        return

    def days_indexes(self, day):
        day = f"Today is the {day}th day of {self.name}'s life"
        print(f"{day:=^50}", '\n')
        cat_indexes = f"{self.name}'s indexes"
        print(f"{cat_indexes:=^50}", '\n')
        print(f'Money - {self.money}')
        print(f'Hunger - {self.hunger}')
        print(f'Happiness - {self.happiness}')
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        print(f"Breed - {self.breed}")

    def is_alive(self):
        if self.happiness < 0:
            print("Depression....")
            return False
        if self.hunger < 0:
            print("Dead...")
            return False
        if self.money < -500:
            print("Bancrupt...")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Found a new home')
            self.get_home()

        dice = random.randint(1, 4)
        if self.hunger < 10:
            print("I'm hungry")
            self.eat()
        elif self.happiness < 20:
            if self.home.mess > 15:
                print('Clean up the mess')
                self.sleep()
            else:
                print("Let's play")
                self.play()


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


cat_breeds = {
    "Persian": {},
    "Sphynx": {},
    "British Shorthair": {},
    "Siamese": {},
    "Maine Coon": {},
    "Bengal": {}
}
import random


class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brand_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            self.money -= 5
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                self.money -= 5
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.drive += 50
        elif manage == 'food':
            print('I bought food')
            self.money -= 25
            self.home.food += 25
        elif manage == 'delicacies':
            print("You're happy!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today is the {day} day of {self.name}'s life"
        print('\n', f'{day:=^50}', '\n')
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", '\n')
        print(f"Money = {self.money}")
        print(f"Satiety = {self.satiety}")
        print(f"Gladness = {self.gladness}")
        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}', '\n')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", '\n')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -200:
            print('Bankrupt')
            return False

    def live(self, day):
        if self.is_alive() == False:
            return
        if self.home == None:
            print('Settled in the home')
            self.get_home()
        if self.car == None:
            self.get_car()
            print(f'I want a {self.car.brand} car')
        if self.job == None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job of {self.job.job}, salary {self.job.salary}")
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if dice == 1:
            self.eat()
        if dice == 2:
            self.work()
        if dice == 3:
            self.shopping('food')
        if dice == 4:
            self.chill()
        if self.satiety < 20:
            print("I'll go to eat")
            self.eat()
        if self.gladness < 10:
            print("I'm gonna chill")
            self.chill()
        if self.money < 20:
            print("I'm gonna work")
            self.work()
        if self.home.mess > 0:
            print("I need to clean my house")
            self.clean_home()
        if self.home.food < 1:
            print("I need to buy some food")
            self.shopping('food')


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'consumption': 6},
                'Lada': {'fuel': 50, 'strength': 40, 'consumption': 10},
                'Volvo': {'fuel': 70, 'strength': 150, 'consumption': 8},
                'Ferrari': {'fuel': 80, 'strength': 120, 'consumption': 14}}

job_list = {'Java developer': {'salary': 50, 'gladness_less': 10},
            'Python developer': {'salary': 40, 'gladness_less': 15},
            'C++ developer': {'salary': 55, 'gladness_less': 25},
            'Rust developer': {'salary': 70, 'gladness_less': 1}}

luz = Human('Luz')

for day in range(1, 8):
    if luz.live(day) == False:
        break

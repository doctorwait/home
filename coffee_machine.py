from time import sleep
from random import choice, randint


class IngredientDescriptor:
    """
    Manages the ingredients in the coffee machine class.
    """
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Drink:
    """
        For each drink - 200 ml of water (except for espresso and ML, there are 25 ml of water each). Recipes:
        Americano: 2 grams of coffee.
        Latte: 2 grams of coffee, 20 grams of milk and 4 grams of sugar.
        Cappuccino: 2 grams of coffee, 10 grams of milk and 2 grams of sugar.
        Espresso: 2 grams of coffee and 25 ml of water.
        Machine learning: charge before the webinar, 4 grams of coffee, 4 grams of sugar, 25 ml of water.
    """

    def __init__(self, coffee, milk, sugar, water):
        """
        When creating a class, we indicate how many ingredients are required per serving.
        """
        self.coffee = coffee
        self.milk = milk
        self.sugar = sugar
        self.water = water
        self.description = ''

    def change_recipe(self, coffee=0, milk=0, sugar=0, water=0, coffee_flag=False,
                      milk_flag=False, sugar_flag=False, water_flag=False):
        if coffee_flag:
            self.coffee = coffee
        if milk_flag:
            self.milk = milk
        if sugar_flag:
            self.sugar = sugar
        if water_flag:
            self.water = water

    def what_needs_to_make_drink(self, num_of_drinks=1):
        """
        Coffee-milk-sugar-water
        """
        return list(map(lambda x: x * num_of_drinks, (self.coffee, self.milk, self.sugar, self.water)))

    def __repr__(self):
        return self.__name__

    def get_info(self):
        divisor = '---'
        return divisor + str(self) + divisor + '\n' + self.description


class Americano(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Americano'
        self.description = "Classic taste.\nBlack coffee without sugar and milk.\nRecipe: 2 tsp. coffee. Yes, that's all."


class Latte(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Latte'
        self.description = 'Very soft and milky coffee - \nfor those who like it sweeter.\n' \
                           'Recipe: 2 tsp coffee, 20 ml milk, 4 tsp sugar'


class Capuccino(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Capuccino'
        self.description = "The barista's favorite.\nTake two to please him.\n" \
                           "Recipe: 2 tsp coffee, 10 ml milk, 2 tsp sugar"


class Espresso(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Espresso'
        self.description = 'For gourmets.\nReveal the entire flavor bouquet of grain.\nRecipe: 2 tsp. coffee, 25 ml water'


class MLDrink(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'SUPERENERGIZING'
        self.description = "New!\nYou won't be a pro without it.\nRecipe: 4 tsp. coffee, 4 tsp sugar, 25 ml water"


class CoffeeMachine:
    sugar = IngredientDescriptor()
    coffee = IngredientDescriptor()
    water = IngredientDescriptor()
    milk = IngredientDescriptor()
    cups = IngredientDescriptor()

    def __init__(self, sugar=100, coffee=100, water=10000, milk=1000, cups=50):
        """
        When initializing the coffee machine, the maximum capacity of the ingredients is indicated, i.e. their full supply.
        """
        self.coffee = coffee
        self.milk = milk
        self.sugar = sugar
        self.water = water
        self.cups = cups  # В одном стаканчике помещается 250 мл напитка
        self.americano = Americano(2, 0, 0, 200)
        self.latte = Latte(2, 20, 4, 250)
        self.capuccino = Capuccino(2, 10, 2, 200)
        self.espresso = Espresso(2, 0, 0, 25)
        self.ml_drink = MLDrink(4, 0, 4, 25)
        self.__password = 'Пароль'

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def __setattr__(self, key, value):
        if key in ('sugar', 'coffee', 'water', 'milk', 'cups') and isinstance(value, int) and value >= 0:
            return super().__setattr__(key, value)
        elif key not in ('sugar', 'coffee', 'water', 'milk', 'cups'):
            return super().__setattr__(key, value)

    def sleeper(self, sec=0.03):
        """
        Simulates the operation of an analog coffee machine.
        """
        variations = ("Thinking", "Calculating", "Think out", "Trying not to break", "Hacking the database", "Copying data",
                       "I extract the root", "I burst at the seams")
        print(choice(variations), end='')
        for dot in '..........':
            print(dot, end='')
            sleep(sec * randint(1, 9))
        print()

    def get_drinks(self):
        """
        Returns a tuple of the current drinks.
        """
        return self.americano, self.espresso, self.capuccino, self.latte, self.ml_drink

    def __reset_machine(self, alls=False, coffee=0, milk=0, sugar=0, water=0, cups=0):
        """
        Admin tool, updates assortment to default numbers. The possibility of a point update is laid.
        """
        if alls:
            coffee, milk, sugar, water, cups = (100, 1000, 100, 10000, 50)
        self.coffee = coffee if coffee else self.coffee
        self.milk = milk if milk else self.milk
        self.sugar = sugar if sugar else self.sugar
        self.water = water if water else self.water
        self.cups = cups if cups else self.cups

    def visualize_possibilities(self):
        """
        Returns a list of available drinks.
        """
        what_we_have = (self.coffee, self.milk, self.sugar, self.water)
        res = []
        for drink in self.get_drinks(): # Пробегаемся по всем напиткам
            current_drink_recipe = drink.what_needs_to_make_drink()
            if all(map(lambda x: x[0] <= x[1], zip(current_drink_recipe, what_we_have))):
                res.append(drink.__name__)
        return res

    def max_possible_one_drink(self, drink):
        """
        How many units of a particular drink can we make based on current stock.
        """
        what_we_have = (self.coffee, self.milk, self.sugar, self.water)
        return max(list(map(lambda x: x[0] // x[1] if x[1] != 0 else 1, zip(what_we_have, drink.what_needs_to_make_drink()))))

    def display_menu(self):
        """
        User start menu. Appears on the screen once.
        """
        print("Good afternoon! Here is the menu of our coffee machine.")
        current_possibilities = self.visualize_possibilities()
        print(f'Choose a drink.\nThere is {self.cups} pcs of cups, and the following drinks:')
        for drink in self.get_drinks():
            if str(drink) in current_possibilities:
                self.sleeper()
                print(drink.get_info())

    def user_choise(self):
        """
        The function contains the drink selection logic. 
        """
        lst = self.visualize_possibilities()
        if len(lst) == 0:
            print('We're sorry, we're out of beverage ingredients, please contact a service technician. ;(')
            return 'Cancel'
        menu = '; '.join([item + ' - ' + str(lst.index(item) + 1) for item in lst])
        ch = num = -1
        while not -1 < ch <= len(lst):
            ch = int(input('Enter a number to select a drink (Enter 0 to cancel) : ' + menu + ' --> '))
            if ch == 0:
                return 'Cancel'
        self.sleeper()
        for drink in self.get_drinks():
            if str(drink) == lst[ch - 1]:
                ch = drink
                break
        max_possible_this_drink = min(self.max_possible_one_drink(ch), self.cups)
        while not -1 < num <= max_possible_this_drink:
            num = int(input(f'Available: {max_possible_this_drink} pcs. How much do we cook? (Enter 0 to cancel) '))
            if num == 0:
                return 'Cancel'
        return ch, num

    def cook(self, drink, num):
        """
        To "brew" a drink means to reduce the current stock of food.
        """
        needs = drink.what_needs_to_make_drink(num)
        self.coffee -= needs[0]
        self.milk -= needs[1]
        self.sugar -= needs[2]
        self.water -= needs[3]
        self.cups -= num

    def initialize_user_interface(self):
        """
        Manages the user interface.
        """
        self.display_menu()
        while True:
            choose = self.user_choise()
            if choose == 'Cancel':
                turn_off = input('Are you sure you want to end the service? Y/N --> ')
                if turn_off == 'Y':
                    print('We were happy to help you!')
                    break
                else:
                    print("Let's try again!")
                    continue
            drink, num = choose
            self.cook(drink, num)
            self.sleeper(0.09)
            print(f'You can pick up {num} psc {str(drink).lower()}.')

    def initialize_specialist_interface(self):
        """
        Controls the service personnel interface.
        """
        print('Welcome to the coffee machine control menu!')
        password, counter = input(f'Enter the "{self.__password}" to access the control of the coffee machine: '), 3
        while password != self.password and counter != 0:
            password = input(f'Remaining tries: {counter}.\nEnter "{self.__password}": ')
            counter -= 1
        if password != self.__password:
            print('The system is locked for 30 seconds. Try later.')
            sleep(0.5)
            return
        print('Login confirmed.')
        while True:
            choise = int(input("What do you want to do?\nExit interface: 0\nReplenish all supplies: 1\n"
                                "Change administrator password: 2\n"))
            if choise == 0:
                last = input('Do you want to initialize the user interface? Y/N --> ')
                if last == 'Y':
                    self.initialize_user_interface()
                    break
                else:
                    break
            elif choise == 1:
                self.__reset_machine(alls=True)
                print('Stocks successfully replenished.')
            elif choise == 2:
                self.password = input('Enter a new password: ')
                print('Password successfully registered in the system.')


machine = CoffeeMachine()
#machine.initialize_user_interface()
machine.initialize_specialist_interface()
machine.initialize_specialist_interface()

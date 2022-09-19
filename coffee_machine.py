from time import sleep
from random import choice, randint


class IngredientDescriptor:
    """
    Управляет ингредиентами в классе кофе-машины.
    """
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Drink:
    """
        На каждый напиток - 200 мл воды (кроме эспрессо и МЛ, там по 25 мл воды). Рецепты:
        Американо: 2 гр кофе.
        Латте: 2 гр кофе, 20 гр молока и 4 гр сахара.
        Капуччино: 2 гр кофе, 10 гр молока и 2 гр сахара.
        Эспрессо: 2 гр кофе и 25 мл воды.
        Машинное обучение: заряд перед вебинаром, 4 гр кофе, 4 гр сахара, 25 мл воды.
    """

    def __init__(self, coffee, milk, sugar, water):
        """
        При создании класса, указываем, сколько ингредиентов требуется на одну порцию.
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
        Кофе-молоко-сахар-вода
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
        self.__name__ = 'Американо'
        self.description = 'Классика вкуса.\nЧёрный кофе без сахара и молока.\nРецепт: 2 ч.л. кофе. Да, это всё.'


class Latte(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Латте'
        self.description = 'Очень мягкий и молочный кофе -\nтем, кто любит послаще.\n' \
                           'Рецепт: 2 ч.л. кофе, 20 мл молока, 4 ч.л. сахара'


class Capuccino(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Капучино'
        self.description = 'Конёк бариста.\nВозьми два, чтобы порадовать его.\n' \
                           'Рецепт: 2 ч.л. кофе, 10 мл молока, 2 ч.л. сахара'


class Espresso(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'Эспрессо'
        self.description = 'Для гурманов.\nРаскроет весь вкусовой букет зерна.\nРецепт: 2 ч.л. кофе, 25 мл воды'


class MLDrink(Drink):
    def __init__(self, coffee, milk, sugar, water):
        super().__init__(coffee, milk, sugar, water)
        self.__name__ = 'СУПЕРБОДРЯЩИЙ'
        self.description = 'Новинка!\nБез него ты не станешь профи.\nРецепт: 4 ч.л. кофе, 4 ч.л. сахара, 25 мл воды'


class CoffeeMachine:
    sugar = IngredientDescriptor()
    coffee = IngredientDescriptor()
    water = IngredientDescriptor()
    milk = IngredientDescriptor()
    cups = IngredientDescriptor()

    def __init__(self, sugar=100, coffee=100, water=10000, milk=1000, cups=50):
        """
        При инициализации кофе-автомата, указывается максимальная вместимость ингредиентов, т.е. их полный запас.
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
        Имитирует работу аналоговой кофе-машины.
        """
        variations = ("Думаю", "Вычисляю", "Соображаю", "Пытаюсь не сломаться", "Взламываю базу", "Копирую данные",
                      "Извлекаю корень", "Трещу по швам")
        print(choice(variations), end='')
        for dot in '..........':
            print(dot, end='')
            sleep(sec * randint(1, 9))
        print()

    def get_drinks(self):
        """
        Возвращает кортеж из текущих напитков (не текущих из кофе-машины, а присутствующих в ней). 
        """
        return self.americano, self.espresso, self.capuccino, self.latte, self.ml_drink

    def __reset_machine(self, alls=False, coffee=0, milk=0, sugar=0, water=0, cups=0):
        """
        Инструмент администратора, обновляет ассортимент до дефолтных цифр. Заложена возможность точечного обновления. 
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
        Выдаёт список из доступных напитков.
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
        Сколько единиц конкретного напитка мы можем сделать, исходя из текущих запасов.
        """
        what_we_have = (self.coffee, self.milk, self.sugar, self.water)
        return max(list(map(lambda x: x[0] // x[1] if x[1] != 0 else 1, zip(what_we_have, drink.what_needs_to_make_drink()))))

    def display_menu(self):
        """
        Стартовое меню пользователя. Появляется на экране один раз. 
        """
        print("Добрый день! Перед вами - меню нашей кофе-машины.")
        current_possibilities = self.visualize_possibilities()
        print(f'Выберите напиток.\nЕсть {self.cups} шт. стаканчиков, и следующие напитки:')
        for drink in self.get_drinks():
            if str(drink) in current_possibilities:
                self.sleeper()
                print(drink.get_info())

    def user_choise(self):
        """
        Функция содержит логику выбора напитка. 
        """
        lst = self.visualize_possibilities()
        if len(lst) == 0:
            print('К сожалению, ингредиенты для напитков закончились, обратитесь к специалисту техобслуживания ;(')
            return 'Отмена'
        menu = '; '.join([item + ' - ' + str(lst.index(item) + 1) for item in lst])
        ch = num = -1
        while not -1 < ch <= len(lst):
            ch = int(input('Введите число для выбора напитка (Введите 0 для отмены) : ' + menu + ' --> '))
            if ch == 0:
                return 'Отмена'
        self.sleeper()
        for drink in self.get_drinks():
            if str(drink) == lst[ch - 1]:
                ch = drink
                break
        max_possible_this_drink = min(self.max_possible_one_drink(ch), self.cups)
        while not -1 < num <= max_possible_this_drink:
            num = int(input(f'Доступно: {max_possible_this_drink} штук. Сколько готовим? (Введите 0 для отмены) '))
            if num == 0:
                return 'Отмена'
        return ch, num

    def cook(self, drink, num):
        """
        "Приготовить" напиток означает уменьшить текущие запасы продуктов. 
        """
        needs = drink.what_needs_to_make_drink(num)
        self.coffee -= needs[0]
        self.milk -= needs[1]
        self.sugar -= needs[2]
        self.water -= needs[3]
        self.cups -= num

    def initialize_user_interface(self):
        """
        Управляет пользовательским интерфейсом.
        """
        self.display_menu()
        while True:
            choose = self.user_choise()
            if choose == 'Отмена':
                turn_off = input('Вы уверены, что хотите завершить обслуживание? Y/N --> ')
                if turn_off == 'Y':
                    print('Были рады вам помочь!')
                    break
                else:
                    print('Попробуем выбрать снова!')
                    continue
            drink, num = choose
            self.cook(drink, num)
            self.sleeper(0.09)
            print(f'Вы можете забрать {num} шт. {str(drink).lower()}.')

    def initialize_specialist_interface(self):
        """
        Управляет интерфейсом обслуживающего персонала. 
        """
        print('Добро пожаловать в управление кофе-машиной!')
        password, counter = input(f'Введите "{self.__password}" для доступа к управлению кофе-машиной: '), 3
        while password != self.password and counter != 0:
            password = input(f'Осталось попыток: {counter}.\nВведите "{self.__password}": ')
            counter -= 1
        if password != self.__password:
            print('Система заблокирована на 30 секунд. Попробуйте позже.')
            sleep(0.5)
            return
        print('Вход подтверждён.')
        while True:
            choise = int(input("Что вы хотите сделать?\nВыйти из интерфейса: 0\nПополнить все запасы: 1\n"
                               "Сменить пароль администратора: 2\n"))
            if choise == 0:
                last = input('Вы хотите инициализировать пользовательский интерфейс? Y/N --> ')
                if last == 'Y':
                    self.initialize_user_interface()
                    break
                else:
                    break
            elif choise == 1:
                self.__reset_machine(alls=True)
                print('Запасы успешно пополнены.')
            elif choise == 2:
                self.password = input('Введите новый пароль: ')
                print('Пароль успешно зарегистрирован в системе.')


machine = CoffeeMachine()
#machine.initialize_user_interface()
machine.initialize_specialist_interface()
machine.initialize_specialist_interface()

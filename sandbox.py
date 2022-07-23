from random import randint

from timer import timer


class MagicSquare:
    def __init__(self, size):
        # Минимальная сторона квадрата - 3, иначе он не считается "магическим"
        self.size = 3 if size <= 2 else size
        # Формируем матрицу для экспериментов и её пустую копию для обнуления
        self.matrix = [[0] * self.size for i in range(self.size)]
        self.matrix_defaulter = list()
        for i in self.matrix:
            self.matrix_defaulter.append(i[:])
        # Максимальное число в ячейке равно квадрату стороны
        self.max_random = self.size * self.size
        # Генерируем координаты точек, лежащих на диагонали
        self.diagonals = self.diagonals_coords()
        # Словарь с информацией о каждом числе - находится ли оно в матрице в конкретный период времени. Можно обнулять.
        self.numbers_dict = dict((i, False) for i in range(1, self.max_random + 1))
        self.numbers_dict_defaulter = dict()
        for i in self.numbers_dict:
            self.numbers_dict_defaulter[i] = False

    @staticmethod
    def sums_of_lines(matrix: list, size: int, results=None):
        """
        Возвращает список из сумм: 1-й и 2-й элементы = суммы по диагоналям, далее N элементов суммы горизонталей, и N
        элементов - по вертикали, где N = стороне квадрата.
        """
        if results is None:
            results = [0]*(size * 2 + 2)
        for i in range(size):
            results[0] += matrix[i][i]
            results[1] += matrix[i][-i - 1]
            for j in range(size):
                results[i + 2] += matrix[i][j]
                results[-i - 1] += matrix[j][i]
        return results

    def get_default_sources(self):
        """
        Обнуляет матрицу и словарь использованных чисел
        """
        self.matrix.clear()
        for i in self.matrix_defaulter:
            self.matrix.append(i[:])
        for i in self.numbers_dict:
            self.numbers_dict[i] = self.numbers_dict_defaulter[i]

    def break_condition(self, switcher_for_diagonals=False):
        """
        Сравнивает все суммы между собой; если они одинаковы - возвращает True.
        Для диагоналей - сравнивает их суммы, возвращает True если одинаковые.
        """
        results = self.sums_of_lines(self.matrix, self.size)
        if switcher_for_diagonals:
            return True if results[0] == results[1] else False
        if not switcher_for_diagonals:
            for i in range(len(results)):
                if results[0] != results[i]:
                    return False
        return True

    def zero_condition(self):
        """
        Возвращает True, если на диагоналях нулей нет.
        """
        for point in self.diagonals:
            x = point[0]
            y = point[1]
            if self.matrix[x][y] == 0:
                return False
        return True

    def edges_condition(self, matrix, numbers_dict, target_number, free_numbers=None):
        """
        После выстраивания диагоналей, проверяет вакантные места и свободные цифры на наличие невозможных комбинаций.
        Возвращает True, если не находит подвохов.
        matrix - Матрица после генерации диагоналей.
        numbers_dict - Словарь с данными о свободных цифрах.
        target_number - Сумма одной из диагоналей - целевое число, должно получаться при суммации на любом направлении.
        """
        if free_numbers is None:
            free_numbers = []
        [free_numbers.append(i) for i in self.numbers_dict if not self.numbers_dict[i]]
        a, b, c, d = matrix[0][0], matrix[0][-1], matrix[-1][0], matrix[-1][-1]
        up, left, right, down = a + b, a + c, b + d, c + d
        # Ищем минимум и максимум
        if up < left:
            if right < down:
                minimum = up if up < right else right
                maximum = down if down > left else left
            else:
                minimum = up if up < down else down
                maximum = right if right > left else left
        else:
            if right < down:
                minimum = left if up < right else right
                maximum = down if down > up else up
            else:
                minimum = left if up < down else down
                maximum = up if up > right else right
        print(free_numbers, minimum, maximum, target_number)
        # Смотрим крайние случаи
        if maximum + free_numbers[0] >= target_number or minimum + free_numbers[-1] < target_number:
            return False
        return True

    def diagonals_coords(self):
        """
        Возвращает множество из кортежей с координатами всех точек на двух диагоналях квадрата. Формат (х, у).
        """
        collection_coords = set()
        for i in range(self.size):
            collection_coords.add((i, i))
            collection_coords.add((self.size - 1 - i, i))
        return collection_coords

    @timer
    def fill_square(self):
        """
        Главная функция; последовательно заливает все ячейки квадрата.
        """
        self.fill_diagonals()
        self.show()
        self.fill_periphery()

    @timer
    def fill_diagonals(self):
        """
        Заливает диагонали квадрата.
        """
        # Пока на диагоналях есть нули:
        while not self.zero_condition():
            x, y = randint(0, self.size - 1), randint(0, self.size - 1)  # Это новые координаты
            #  Если эта координата не лежит на диагонали
            if (x, y) not in self.diagonals:
                continue
            d_number = randint(1, self.max_random)  # Это новое число
            #  Если число для новой позиции уже стоит в другом месте квадрата
            if self.numbers_dict[d_number]:
                continue
            # Для старого числа нужно обнулить его "вакантность" - возможность переиспользования
            if self.matrix[x][y] != 0:
                self.numbers_dict[self.matrix[x][y]] = False
            # Добавляем в матрицу новое число и маркируем его как занятое
            self.matrix[x][y] = d_number
            self.numbers_dict[d_number] = True
            # Если на диагоналях больше нет нулей
            if self.zero_condition():
                # Если суммы не совпадают или в центре 3-х ячеистой матрицы стоит не число 5 - всё заново
                if not self.break_condition(switcher_for_diagonals=True) or (self.size == 3 and self.matrix[1][1] != 5):
                    self.get_default_sources()
                    continue
                elif self.break_condition(switcher_for_diagonals=True):
                    # Целевое число можем посчитать только при условии, что оно одинаковое у обеих диагоналей; считаем:
                    target_number = sum(self.matrix[i][i] for i in range(self.size))
                    # Проверка крайних случаев:
                    if not self.edges_condition(self.matrix, self.numbers_dict, target_number):
                        self.get_default_sources()
                        continue
                    print('Считает диагонали равными:')
                    return

    def fill_periphery(self):
        """
        Заливает точки, не принадлежащие линиям диагоналей.
        """
        print('Начал заливать периферию')

        while not self.break_condition():
            a, b = randint(0, self.size - 1), randint(0, self.size - 1)
            if (a, b) in self.diagonals:
                continue
            number = randint(1, self.max_random)
            self.matrix[a][b] = number
            if self.break_condition():
                return

    def show(self):
        for i in range(self.size):
            print(*self.matrix[i])


res = MagicSquare(5)
res.fill_diagonals()
res.show()

# 2 4 6 8

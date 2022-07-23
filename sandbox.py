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
    def sums_of_lines(matrix: list, size: int, results=None, first_lines_for_success=False):
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
            self.matrix[x][y] = d_number
            self.numbers_dict[d_number] = True
            if self.zero_condition():
                if not self.break_condition(switcher_for_diagonals=True):
                    self.get_default_sources()
                    continue
                elif self.break_condition(switcher_for_diagonals=True):
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

# TODO Возможно, верный алгоритм - при создании диагоналей сразу же заполнять 4 крайние границы квадрата

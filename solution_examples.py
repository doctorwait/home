# Задания к решению подбираются случайным образом, поэтому 
# описанные решения раскрывают только часть моих знаний.


def sum_array(arr): 
    '''
    Функция описывает способ суммации элементов целочисленного массива 
    без учёта в результате крайних по величинам чисел.
    '''
    if arr is None:
        return 0
    elif len(arr) < 3:
        print(len(arr))
        return 0
    else:
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))
        return sum(arr)


def dna_to_rna(dna): 
    '''
    Конвертер ДНК в РНК, на вход принимается вложенный список
    '''
    if len(dna) == 0:
        return 0
    else:
        for nucleic in dna:
            ind = dna.index(nucleic)
            if nucleic == "T":
                if ind == 0:
                    dna = 'U' + dna[1:]
                dna = dna[0:ind] + 'U' + dna[ind+1:]
        return dna


    
def isends(string, ending): 
    '''
    Здесь мы смотрим, заканчивается ли первый строковый аргумент 
    символами из второго (альтернатива .endwith())
    '''
    lend = len(ending)
    sl = string[:-lend]
    res = sl + ending
    return string == res or ending == ''    


def word_ending(x:int, word:str):
    '''
    Функция принимает word, которому нужно заменить окончание,
    и число x, которое является количественным числительным.
    '''
    num10, num100 = x % 10, x % 100
    if x == 0 or 5 <= x <= 20 or 11 <= num100 <= 14 or 5 <= num10 <= 9 or num10 == 0:
        print(x, word + 'ов')
    elif x == 1 or x > 20 and num10 == 1:
        print(x, word)
    elif 2 <= num10 <= 4:
        print(x, word + 'а')
        

def multiply_table(a, b, c, d):
    '''
    Генератор таблицы умножения двух диапазонов чисел, лежащих
    в пределах от a до b и от c до d. Ноль не игнорируется - для 
    числа n выполняется n*0 == 0.
    '''
    print('', *list(range(c, d + 1)), sep='\t')
    for x in range(a, b + 1):
        print(x, end='\t')
        for y in range(c, d + 1):
            print(x * y, end='\t')
        print(sep='\t')
        


'''
Код ниже построчно принимает на вход прямоугольную матрицу, для завершения ввода
пишется слово 'end'. Выводит на печать матрицу той же формы, где каждый элемент
является суммой всех его соседей с четырёх сторон, без учёта самого элемента.
'''
# Заполнение матрицы.
first = [int(x) for x in input().split()]
matrix, res = [], []
while True:
    x = input()
    if x == 'end':
        break
    matrix.append([int(y) for y in x.split()])
matrix.insert(0, first)
lm = len(matrix)

# Проверка на один элемент
if len(first) == 1 and len(matrix) == 1:
    print(first[0]*4)
    
else:
# Копирование матрицы
    for lst in matrix:
        tmp = []
        for item in lst:
            tmp.append(item)
        res.append(tmp)
    
# Заполнение новой матрицы 
    for indlst, lst in enumerate(matrix, 0):
        ll = len(lst)
        for indnum in range(len(lst)):
            res[indlst][indnum] = (matrix[indlst][(indnum - 1) % ll] + matrix[indlst][(indnum + 1) % ll]
            + matrix[(indlst - 1) % lm][indnum] + matrix[(indlst + 1) % lm][indnum])
for lst in res:
    print(*lst, end='\n')


'''
Код ниже открывает файл со строкой в формате число-номер (а3б7в13...) и печатает
в отдельный файл каждую букву столько раз, какое после неё стоит число.
'''

txt = open('dataset_3363_2.txt', 'r')
s1 = txt.read()
txt.close()

num = 0
sym = str
var = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
output = open('result.txt', 'w')


for ind in range(len(s1)):
    if s1[ind] in var and s1[ind + 1] in var:
        num = int(s1[ind]) * 10 + int(s1[ind + 1])
        sym = s1[ind - 1]
        print(sym * num, file=output, end='')
    elif s1[ind] in var and s1[ind + 1] not in var and s1[ind - 1] not in var:
        num = int(s1[ind])
        sym = s1[ind - 1]
        print(sym * num, file=output, end='')
        
        
        
        
        
        

'''
Код ниже считывает в одну строку файл, находит наиболее часто встречающуюся 
последовательность символов (без учёта регистра) и печатает в новый файл
эту последовательность и число - сколько раз она встретилась в исходнике.
'''

# Блок считывания и подготовки к записи (файл создаётся автоматически)
txt = open('dataset_3363_3.txt', 'r')
inp = txt.read()
output = open('result.txt', 'w')

# Контейнер - это кортеж отдельных последовательностей; делим по пробелам и
# сразу же приводим к нижнему регистру
container = tuple(inp.lower().split())
dic_res, temp_key = {}, 0

# Уникальными должны быть наборы последовательностей символов, поэтому мы
# записываем их в ключи словаря, а значения - число повторения для каждого
# ключа.
for ind in range(len(container)):
    temp_key = container.count(container[ind])
    if container[ind] not in dic_res.keys():
        dic_res[container[ind]] = temp_key

# Находим все послед-ти, которые встречаются чаще остальных. Таких может быть
# несколько, поэтому записываем все в промежуточный словарь, из которого 
# по тому же принципу вытаскиваем послед-ть с наименьшим значением.
max_value = max(dic_res.values())
dic_max = {key: value for key, value in dic_res.items() if value == max_value}
min_key = min(dic_max.keys())
dic_end = {key: value for key, value in dic_max.items() if key == min_key}
for key, value in dic_end.items():
    print(key, value, file=output)




'''
Следующий код - пример работы со списком, в который вложен список списков.
На вход подаётся количество матчей (отдельно) и результаты каждого матча
в формате "Спартак;9;Зенит;10". Далее формируется статистика.
'''

games = int(input())
games_res = games # Доп. хранилище количества матчей
lst = [] # Общий лист всех матчей, где каждый - в списке
teams, result = [], []

# Заполняем общий лист всеми данными
while games > 0:
    tmp = []
    s = str(input()).split(';')
    lst.append([[s[0], int(s[1])], [s[2], int(s[3])]])
    if s[0] not in teams:
        teams.append(s[0])
    if s[2] not in teams:
        teams.append(s[2])
    games -= 1
    
# Делаем список с итоговой статистикой. Индексы команды в листе команд и её результатов - совпадают.
for ind in range(len(teams)):
    result.append([teams[ind], 0, 0, 0, 0, 0]) # Всего_игр Побед Ничьих Поражений Всего_очков

for ind_team in range(len(teams)): # Для каждой команды
    for match in range(len(lst)): # Для каждого матча (список списков)
        score_left, score_right = lst[match][0][1], lst[match][1][1]
        team_left, team_right = lst[match][0][0], lst[match][1][0]
        is_team_left, is_team_right = team_left == teams[ind_team], team_right == teams[ind_team]
        if is_team_left or is_team_right: # "Всего игр"
            result[ind_team][1] += 1
        if score_left > score_right and is_team_left: # Зачёт победы левой команде
            result[ind_team][2] += 1
            result[ind_team][5] += 3
        elif score_left == score_right and is_team_left: # Зачёт ничьей левой команде
            result[ind_team][3] += 1
            result[ind_team][5] += 1
        elif score_left < score_right and is_team_left: # Зачёт поражения левой команде
            result[ind_team][4] += 1
        elif score_right > score_left and is_team_right: # Зачёт победы правой команде
            result[ind_team][2] += 1
            result[ind_team][5] += 3
        elif score_right == score_left and is_team_right: # Зачёт ничьей правой команде
            result[ind_team][3] += 1
            result[ind_team][5] += 1
        elif score_right < score_left and is_team_right: # Зачёт поражения правой команде
            result[ind_team][4] += 1
    
for match in result:
    print(match[0] + ':', match[1], sep='', end=' ')
    print(*match[2:6], end='\n')
    
    
    
'''
Функция принимает на вход произвольную строку и делает все буквы в словах длиннее 2-х 
символов прописными, а первую - заглавной.
'''
def drop_cap(tar):
    mouse = []
    if len(tar) == 0:
        return ""
    elif len(tar) <= 2:
        return tar.lower()
    mouse.append(tar[0])
    for i in range(1, len(tar)):
        if tar[i] != ' 'and mouse[-1][-1] != ' ' or tar[i] == ' 'and mouse[-1][-1] == ' ':
            mouse[-1] = mouse[-1] + tar[i]
        else:
            mouse.append(tar[i])
    for ind in range(len(mouse)):
        if len(mouse[ind]) > 2:
            mouse[ind] = mouse[ind].lower().title()
    return ''.join(mouse)
 
 
 
 '''
 Задача с курса по Питону. Код рисует закрученную вправо спираль в виде квадрата со стороной,
 равной отправленному пользователем числу n. Спираль содержит в себе числа от 1 до n*n. В решении
 я решил избежать рекурсии и проверок if/else, а также, при возможности, вставлял блоки списков
 целиком, без поэлементного переноса.
 '''
 n = int(input())

mat = [[0]*n for i in range(n)]
lst = list(range(1, n*n + 1))
lst = lst[::-1]

# Заполняем первую строчку
for i in range(n):
    mat[0][i] = lst.pop()
    
counter = 1

while counter < n:
    for i in range(counter, n):  # Сверху вниз
        mat[i][n-1] = lst.pop()
        
    mat[n-1][counter-1 : n-1] = lst[-(n-counter) : ]  # Справа налево
    del lst[-(n-counter) : ]
    n -= 1
    
    for i in range(n-1, counter-1, -1):  # Идём наверх
        mat[i][counter-1] = lst.pop()
    
    mat[counter][counter:n] = lst[-(n-counter):][::-1]  # Идём направо
    del lst[-(n-counter):]
    counter += 1

for i in mat:
    print(*i)
    
    
    
'''
Функция ниже берёт на вход список, и возвращает новый список, где каждый элемент
является суммой всех элементов исходного списка, пример:
[0, 1, 2, 3] - исходник, и он "разбивается" на такие составляющие:
        [1, 2, 3]
        [2, 3]
        [3]
        []
Суммирование происходит по горизонтали, результат в этом примере: [6, 6, 5, 3, 0]
Note: представлено два варианта решения
'''

# Однопроходное решение с экономией машинных ресурсов (в отличие от рекурсивного):

def parts_sums(ls):
    res = []
    if ls == []:
        return [0]
    s = sum(ls)
    res.append(s)
    for item in range(len(ls)):
        res.append(s - ls[item])
        s -= ls[item]
    return res
    
    
# Решение через рекурсию:
 
def parts_sums(ls, res=[]):
    if len(ls) == 0:
        res.append(0)
        return res
    res.append(sum(ls))
    parts_sums(ls[1:], res)
    return res


'''
А здесь одна из задач курса по Питону на Степике. Сама суть, конечно, спорная:
авторы заставляют парсить URL при помощи регулярных выражений. Ну, как пример
владения ими, и для acchievement, оставлю это здесь.
'''
import re
import requests

# Формируем контент сайта в виде списка строк
content = requests.get(input()).text.strip()
match = re.findall(r"<a(?:.*)?href=[^ ](?P<q>[\'\"])??(?:.*?:\/\/)?(?P<find>\w[\w\d.-]*)", content)

raw_res = set()
[raw_res.add(i[1]) for i in match]

# Печать из такого выражения, говорят, не очень хороший тон ;) Главное, что
# я это знаю. А применяю для того, чтобы закрепить структуру.
[print(i) for i in sorted(list(raw_res))]



'''
Два класса ниже - реализация двусвязного списка. Я решил обойтись без рекурсии,
чтобы перебирать данные в таком списке - для этого, я реализовал нумерацию
экземпляров.
'''
class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def set_data(self, data):
        self.__data = data

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def add_obj(self, obj):
        if self.head:
            temp = obj
            temp.set_prev(self.tail)
            self.tail.set_next(temp)
            self.tail = temp
        else:
            self.head = obj
            self.tail = obj

    def remove_obj(self):
        if self.tail.get_prev():
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
        else:
            self.tail = None
            self.head = None

    def get_data(self):
        result = []
        obj = self.head
        while obj:
            result.append(obj.get_data())
            obj = obj.get_next()
        return result
        

'''
Возвращаемся на Codewars ;) Здесь у нас декоратор, который сохраняет результаты
работы функции, чтобы не пересчитывать по много раз.
'''

from functools import wraps


def memoize(func, results=None):
    results = {} if results is None else results
    @wraps(func)
    def wrapper(value):
        nonlocal results
        if value not in results:
            results[value] = func(value)
        return results[value]
    return wrapper
    

'''
Пример работы с requests, BeautifulSoup, Pandas, для опытов взял страничку Вики
'''
import requests
import pandas
from bs4 import BeautifulSoup


address = 'https://ru.wikipedia.org/wiki/250_%D0%BB%D1%83%D1%87%D1%88%D0%B8%D1%85_%D1%84%D0%B8%D0%BB%D1%8C%D0%BC%' \
          'D0%BE%D0%B2_%D0%BF%D0%BE_%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8_IMDb'

wiki = requests.get(address)  # Получаем объект
wiki_text = wiki.text  # Вытаскиваем текст
wiki_soup = BeautifulSoup(wiki_text, 'html.parser')  # Парсим
wiki_raw = wiki_soup.body.table.text.split('\n')[7:]  # Вытаскиваем таблицу в виде строки
wiki_splitted = []
for i in range(len(wiki_raw)):
    if wiki_raw[i] != '':
        wiki_splitted.append(wiki_raw[i])  # Формируем список из этой строки без лишних символов
wiki_lines = [wiki_splitted[i + 1: i + 5] for i in range(0, 1250, 5)]  # Формируем список списков построчно

wiki_formatted_data = pandas.DataFrame(wiki_lines)  # Делаем датафрейм
wiki_formatted_data.columns = ['Название фильма', 'Год', 'Режиссёр', 'Жанр по версии IMDb']  # Форматируем датафрейм
wiki_formatted_data.index = pandas.RangeIndex(start=1, stop=251, step=1)

# Десять лучших фильмов
print(wiki_formatted_data.loc[1:11])

# Выбор по жанрам
genres_list = [i for i in wiki_formatted_data['Жанр по версии IMDb'].unique()]
genres_set = set()
for row in genres_list:
    [genres_set.add(i.strip().lower()) for i in row.split(',')]
print('\tДоступные жанры:')
for i in genres_set:
    print(i.capitalize())
while True:
    choice = input('\n\tВыберите жанр: ').lower()
    if choice in genres_set:
        print('\tВот доступные фильмы: ')
        for row in wiki_formatted_data.iloc:
            if choice in row['Жанр по версии IMDb'].lower():
                print(row)
        final = input('\tПродолжим? Д/Н --> ')
        if final == 'Д':
            continue
        else:
            break
    else:
        final2 = input('Выбранного жанра в списке нет. Продолжим? Д/Н --> ')
        if final2 == 'Д':
            continue
        else:
            break

# Выборка по времени - насколько я понял, речь о годе выхода фильма
years = input('Введите год фильма (или диапазон лет, две цифры через пробел, прим. "1990 2010"  ')
years_form = years.strip().split()
if len(years_form) == 2:
    y_start, y_stop = [int(i) for i in years_form]
    for row in wiki_formatted_data.iloc:
        if y_start <= int(row['Год']) <= y_stop:
            print(row)
else:
    years_form = int(years_form[0])
    for row in wiki_formatted_data.iloc:
        if int(row['Год']) == years_form:
            print(row)

# Количество фильмов по режиссёрам
print('Количество режиссёров: ', len(set([i for i in wiki_formatted_data['Режиссёр'].unique()])))

# Количество фильмов по жанрам (у нас такие данные уже есть, но т.к. жанры в основном составные, то выборка не точна)
print('Количество уникальных жанров: ', len(genres_set))

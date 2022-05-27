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


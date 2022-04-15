# Задания к решению подбираются случайным образом, поэтому описанные решения раскрывают только часть моих знаний.


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
        

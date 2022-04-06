# Задания к решению подбираются случайным образом, поэтому описанные решения раскрывают только часть моих знаний.


def sum_array(arr): # Функция описывает способ суммации элементов целочисленного массива без учёта в результате крайних по величинам чисел.
    if arr is None:
        return 0
    elif len(arr) < 3:
        print(len(arr))
        return 0
    else:
        arr.pop(arr.index(max(arr)))
        arr.pop(arr.index(min(arr)))
        return sum(arr)


def dna_to_rna(dna): # Конвертер ДНК в РНК, на вход принимается вложенный список
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


def isends(string, ending): # Здесь мы смотрим, заканчивается ли первый строковый аргумент символами из второго (альтернатива .endwith())
    lend = len(ending)
    sl = string[:-lend]
    res = sl + ending
    return string == res or ending == ''    

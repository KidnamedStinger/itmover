a = []
count = 0
pref = 0

def linguessnumber(target, start, finish, count = count):
    """ функция ищет загаданное число линейным поиском и возвращает количество шагов и само число """

    for i in range(start, finish+1):
        a.append(i)

    for i in range(len(a)):
        if a[i] == target:
            count += 1
            break
        else:
            count += 1
    return(target, count)


def binguessnumber(target, start, finish, count = count):
    
    """ функция ищет загаданное число бинарным поиском и вовзращает количество шагов и само число """
    
    for i in range(start, finish+1):
        a.append(i)
        
    """ индексы первого, среднего и последнего эелементов списка """
    
    low = 0
    mid = len(a) // 2
    high = len(a) - 1
    
    while a[mid] != target and low <= high:
        
        if target > a[mid]:
            low = mid + 1
            count += 1
        else:
            high = mid - 1
            count += 1
        mid = (low + high) // 2
        
    if low > high:
        return(none, none)
    else:
        return(target, count)


def main(target = int(input()), start = int(input()), finish = int(input()), pref = int(input())):

    """ переменная pref отвечает за выбор предпочтительного способа поиска загаданного числа, 1 - бинарный, 2 - линейный """
    if pref == 1:
        target, count = binguessnumber(target, start, finish)
        
    if pref == 2:
        target, count = linguessnumber(target, start, finish)
    
    return(target, count)

print(main())



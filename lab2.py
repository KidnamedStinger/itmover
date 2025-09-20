a = []
count = 0

def binguessnumber(target, start, finish, count  = count):
    # создание списка случайных чисел по указанному интервалу
    for i in range(start, finish+1):
        a.append(i)
    # индексы первого, последнего и среднего чисел
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


def main(target = int(input()), start = int(input()), finish = int(input())):

    target, count = binguessnumber(target, start, finish)
    
    return(target, count)

print(main())

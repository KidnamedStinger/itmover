def guessnumber(target: int, dist: list[int], pref: str) -> list:
    """
    функция угадывания числа по выбранному алгоритму

    "linear" - линейный поиск
    "binary" - бинарный поиск

    """
    sortdist = sorted(dist)

    count = 0

    if pref == "linear":
        for number in range(len(dist)):
            count += 1
            if number == target:
                return number, count
    elif pref == "binary":
        low = 0
        high = len(sortdist) - 1
        mid = (low + high) // 2
        while low <= high:
            count += 1
            if sortdist[mid] == target:
                return sortdist[mid], count
            elif sortdist[mid] > target:
                high = mid - 1
            elif sortdist[mid] < target:
                low = mid + 1
    else:
        print("ошибка выбора поиска")

    return -1, count

def main() -> list:
    "Функция получения ввода с клавиатуры"
    target = int(input("Введите искомое число = "))
    start = int(input("Введите начало списка = "))
    end = int(input("Введите конец списка = "))
    pref = input("Метод угадывания (linear|binary) = ")

    dist = list(range(start, end+1))

class TestMath(unittest.TestCase):
    def test_bin_positive(self):
        self.assertEqual(guessnumber(7, [2,3,4,5,6,7,8,9,10], "binary"), (6, 1))

    def test_bin_negative_and_positive(self):
        self.assertEqual(guessnumber(-4, [-6,-5,-4,-3,-2,-1,0,1,2,3,4], "binary"), (-1, 1))

    def test_bin_target_not_in_list(self):
        self.assertEqual(guessnumber(1, [2,3,4], "binary"), (-1, 2))

    def test_lin_positive(self):
        self.assertEqual(guessnumber(1, [2,3,4,5,6,7,8,9,10], "linear"), (3, 2))

    def test_lin_negative_and_positive(self):
        self.assertEqual(guessnumber(-4, [-6,-5,-4,-3,-2,-1,0,1,2,3,4], "linear"), (-4, 3))

    def test_lin_target_not_in_list(self):
        self.assertEqual(guessnumber(1, [2,3,4], "linear"), (-1, 3))

unittest.main(argv=[''], verbosity=2, exit=False)    
    




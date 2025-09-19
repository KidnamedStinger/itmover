import unittest

def summa(nums, target):
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            if j == i:
                pass
            else:
                b = nums[j]
                if a + b == target:
                    return [i, j]
    return "Пары нет"

class TestMath(unittest.TestCase):
    def test1(self):
        self.assertEqual(summa([3, 3], 6), [0, 1])

    def test2(self):
        self.assertEqual(summa([2,7,11,15], 9), [0, 1])

    def test3(self):
        self.assertEqual(summa([3,2,4], 6), [1, 2])

unittest.main(argv=[''], verbosity=2, exit=False)

    



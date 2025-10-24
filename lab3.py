import unittest

# вариант 5

def gen_bin_tree(height: int = 6, root: int = 5) -> dict:
    """
    Рекурсивно строит бинарное дерево заданной высоты с указанным корнем.
    Левый потомок вычисляется по формуле: root**2
    Правый потомок вычисляется по формуле: root-2

    """

    if height <= 1:
        return {"value": root, "left": None, "right": None}

    left_start = root ** 2
    right_start = root - 2

    left_subtree = gen_bin_tree(height - 1, left_start)
    right_subtree = gen_bin_tree(height - 1, right_start)

    return {
        "value": root,
        "left": left_subtree,
        "right": right_subtree
    }


tree = gen_bin_tree(height=6, root=5)
print(tree)


class TestMath(unittest.TestCase):

    def test_root_easy(self):
        self.assertEqual(gen_bin_tree(1, 5), ({'value': 5, 'left': None, 'right': None}))
    def test_root_harder(self):
        self.assertEqual(gen_bin_tree(2, 5), ({'value': 5, 'left': {'value': 25, 'left': None, 'right': None}, 'right': {'value': 3, 'left': None, 'right': None}}))
    def test_root_hardest(self):
        self.assertEqual(gen_bin_tree(6, 5), ({'value': 5, 'left': {'value': 25, 'left': {'value': 625, 'left': {'value': 390625, 'left': {'value': 152587890625, 'left': {'value': 23283064365386962890625, 'left': None, 'right': None}, 'right': {'value': 152587890623, 'left': None, 'right': None}}, 'right': {'value': 390623, 'left': {'value': 152586328129, 'left': None, 'right': None}, 'right': {'value': 390621, 'left': None, 'right': None}}}, 'right': {'value': 623, 'left': {'value': 388129, 'left': {'value': 150644120641, 'left': None, 'right': None}, 'right': {'value': 388127, 'left': None, 'right': None}}, 'right': {'value': 621, 'left': {'value': 385641, 'left': None, 'right': None}, 'right': {'value': 619, 'left': None, 'right': None}}}}, 'right': {'value': 23, 'left': {'value': 529, 'left': {'value': 279841, 'left': {'value': 78310985281, 'left': None, 'right': None}, 'right': {'value': 279839, 'left': None, 'right': None}}, 'right': {'value': 527, 'left': {'value': 277729, 'left': None, 'right': None}, 'right': {'value': 525, 'left': None, 'right': None}}}, 'right': {'value': 21, 'left': {'value': 441, 'left': {'value': 194481, 'left': None, 'right': None}, 'right': {'value': 439, 'left': None, 'right': None}}, 'right': {'value': 19, 'left': {'value': 361, 'left': None, 'right': None}, 'right': {'value': 17, 'left': None, 'right': None}}}}}, 'right': {'value': 3, 'left': {'value': 9, 'left': {'value': 81, 'left': {'value': 6561, 'left': {'value': 43046721, 'left': None, 'right': None}, 'right': {'value': 6559, 'left': None, 'right': None}}, 'right': {'value': 79, 'left': {'value': 6241, 'left': None, 'right': None}, 'right': {'value': 77, 'left': None, 'right': None}}}, 'right': {'value': 7, 'left': {'value': 49, 'left': {'value': 2401, 'left': None, 'right': None}, 'right': {'value': 47, 'left': None, 'right': None}}, 'right': {'value': 5, 'left': {'value': 25, 'left': None, 'right': None}, 'right': {'value': 3, 'left': None, 'right': None}}}}, 'right': {'value': 1, 'left': {'value': 1, 'left': {'value': 1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -1, 'left': None, 'right': None}}, 'right': {'value': -1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -3, 'left': None, 'right': None}}}, 'right': {'value': -1, 'left': {'value': 1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -1, 'left': None, 'right': None}}, 'right': {'value': -3, 'left': {'value': 9, 'left': None, 'right': None}, 'right': {'value': -5, 'left': None, 'right': None}}}}}}))

unittest.main(argv=[''], verbosity=2, exit=False)

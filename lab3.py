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


tree = gen_bin_tree(height=4, root=5)
print(tree)


class TestMath(unittest.TestCase):

    def test_root_easy(self):
        self.assertEqual(gen_bin_tree(1, 5), ({'value': 5, 'left': None, 'right': None}))
    def test_root_harder(self):
        self.assertEqual(gen_bin_tree(2, 5), ({'value': 5, 'left': {'value': 25, 'left': None, 'right': None}, 'right': {'value': 3, 'left': None, 'right': None}}))
    def test_root_hardest(self):
        self.assertEqual(gen_bin_tree(4, 5), ({'value': 5, 'left': {'value': 25, 'left': {'value': 625, 'left': {'value': 390625, 'left': None, 'right': None}, 'right': {'value': 623, 'left': None, 'right': None}}, 'right': {'value': 23, 'left': {'value': 529, 'left': None, 'right': None}, 'right': {'value': 21, 'left': None, 'right': None}}}, 'right': {'value': 3, 'left': {'value': 9, 'left': {'value': 81, 'left': None, 'right': None}, 'right': {'value': 7, 'left': None, 'right': None}}, 'right': {'value': 1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -1, 'left': None, 'right': None}}}}))
unittest.main(argv=[''], verbosity=2, exit=False)
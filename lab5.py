import unittest

# 5 вариант
def gen_bin_tree(height: int = 6, root: int = 5, left_branch = lambda x: x ** 2, right_branch = lambda x: x - 2) -> dict:
    
    """
    Нерекурсивно строит бинарное дерево заданной высоты c указанным корнем(Стандартно: height = 6, root = 5).
    Левый потомок(left_branch) вычисляется по заданной формуле(Стандартно: root ** 2)
    Правый потомок(right_branch) вычисляется по заданной формуле(Стандартно: root - 2)
    
    """

    tree = {"value": root, "left": None, "right": None}
    
    queue = [(1, tree)]

    while queue:
        level, node = queue.pop(0)
        if level < height:
            left = {"value": left_branch(node['value']), "left": None, "right": None}
            right = {"value": right_branch(node['value']), "left": None, "right": None}
            node['left'] = left
            node['right'] = right
            queue.append((level + 1, left))
            queue.append((level + 1, right))
    return tree

class TestMath(unittest.TestCase):

    def test_root_easy(self):
        self.assertEqual(gen_bin_tree(1, 5), ({'value': 5, 'left': None, 'right': None}))
    def test_different_root(self):
        self.assertEqual(gen_bin_tree(6, 2), ({'value': 2, 'left': {'value': 4, 'left': {'value': 16, 'left': {'value': 256, 'left': {'value': 65536, 'left': {'value': 4294967296, 'left': None, 'right': None}, 'right': {'value': 65534, 'left': None, 'right': None}}, 'right': {'value': 254, 'left': {'value': 64516, 'left': None, 'right': None}, 'right': {'value': 252, 'left': None, 'right': None}}}, 'right': {'value': 14, 'left': {'value': 196, 'left': {'value': 38416, 'left': None, 'right': None}, 'right': {'value': 194, 'left': None, 'right': None}}, 'right': {'value': 12, 'left': {'value': 144, 'left': None, 'right': None}, 'right': {'value': 10, 'left': None, 'right': None}}}}, 'right': {'value': 2, 'left': {'value': 4, 'left': {'value': 16, 'left': {'value': 256, 'left': None, 'right': None}, 'right': {'value': 14, 'left': None, 'right': None}}, 'right': {'value': 2, 'left': {'value': 4, 'left': None, 'right': None}, 'right': {'value': 0, 'left': None, 'right': None}}}, 'right': {'value': 0, 'left': {'value': 0, 'left': {'value': 0, 'left': None, 'right': None}, 'right': {'value': -2, 'left': None, 'right': None}}, 'right': {'value': -2, 'left': {'value': 4, 'left': None, 'right': None}, 'right': {'value': -4, 'left': None, 'right': None}}}}}, 'right': {'value': 0, 'left': {'value': 0, 'left': {'value': 0, 'left': {'value': 0, 'left': {'value': 0, 'left': None, 'right': None}, 'right': {'value': -2, 'left': None, 'right': None}}, 'right': {'value': -2, 'left': {'value': 4, 'left': None, 'right': None}, 'right': {'value': -4, 'left': None, 'right': None}}}, 'right': {'value': -2, 'left': {'value': 4, 'left': {'value': 16, 'left': None, 'right': None}, 'right': {'value': 2, 'left': None, 'right': None}}, 'right': {'value': -4, 'left': {'value': 16, 'left': None, 'right': None}, 'right': {'value': -6, 'left': None, 'right': None}}}}, 'right': {'value': -2, 'left': {'value': 4, 'left': {'value': 16, 'left': {'value': 256, 'left': None, 'right': None}, 'right': {'value': 14, 'left': None, 'right': None}}, 'right': {'value': 2, 'left': {'value': 4, 'left': None, 'right': None}, 'right': {'value': 0, 'left': None, 'right': None}}}, 'right': {'value': -4, 'left': {'value': 16, 'left': {'value': 256, 'left': None, 'right': None}, 'right': {'value': 14, 'left': None, 'right': None}}, 'right': {'value': -6, 'left': {'value': 36, 'left': None, 'right': None}, 'right': {'value': -8, 'left': None, 'right': None}}}}}}))
    def test_task(self):
        self.assertEqual(gen_bin_tree(6, 5), ({'value': 5, 'left': {'value': 25, 'left': {'value': 625, 'left': {'value': 390625, 'left': {'value': 152587890625, 'left': {'value': 23283064365386962890625, 'left': None, 'right': None}, 'right': {'value': 152587890623, 'left': None, 'right': None}}, 'right': {'value': 390623, 'left': {'value': 152586328129, 'left': None, 'right': None}, 'right': {'value': 390621, 'left': None, 'right': None}}}, 'right': {'value': 623, 'left': {'value': 388129, 'left': {'value': 150644120641, 'left': None, 'right': None}, 'right': {'value': 388127, 'left': None, 'right': None}}, 'right': {'value': 621, 'left': {'value': 385641, 'left': None, 'right': None}, 'right': {'value': 619, 'left': None, 'right': None}}}}, 'right': {'value': 23, 'left': {'value': 529, 'left': {'value': 279841, 'left': {'value': 78310985281, 'left': None, 'right': None}, 'right': {'value': 279839, 'left': None, 'right': None}}, 'right': {'value': 527, 'left': {'value': 277729, 'left': None, 'right': None}, 'right': {'value': 525, 'left': None, 'right': None}}}, 'right': {'value': 21, 'left': {'value': 441, 'left': {'value': 194481, 'left': None, 'right': None}, 'right': {'value': 439, 'left': None, 'right': None}}, 'right': {'value': 19, 'left': {'value': 361, 'left': None, 'right': None}, 'right': {'value': 17, 'left': None, 'right': None}}}}}, 'right': {'value': 3, 'left': {'value': 9, 'left': {'value': 81, 'left': {'value': 6561, 'left': {'value': 43046721, 'left': None, 'right': None}, 'right': {'value': 6559, 'left': None, 'right': None}}, 'right': {'value': 79, 'left': {'value': 6241, 'left': None, 'right': None}, 'right': {'value': 77, 'left': None, 'right': None}}}, 'right': {'value': 7, 'left': {'value': 49, 'left': {'value': 2401, 'left': None, 'right': None}, 'right': {'value': 47, 'left': None, 'right': None}}, 'right': {'value': 5, 'left': {'value': 25, 'left': None, 'right': None}, 'right': {'value': 3, 'left': None, 'right': None}}}}, 'right': {'value': 1, 'left': {'value': 1, 'left': {'value': 1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -1, 'left': None, 'right': None}}, 'right': {'value': -1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -3, 'left': None, 'right': None}}}, 'right': {'value': -1, 'left': {'value': 1, 'left': {'value': 1, 'left': None, 'right': None}, 'right': {'value': -1, 'left': None, 'right': None}}, 'right': {'value': -3, 'left': {'value': 9, 'left': None, 'right': None}, 'right': {'value': -5, 'left': None, 'right': None}}}}}}))


unittest.main(argv=[''], verbosity=2, exit=False)

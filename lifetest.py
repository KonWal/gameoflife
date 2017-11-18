import unittest

class test_cell_updates(unittest.TestCase):
    
    def test_cell_update_overpop(self):
        self.assertEqual(cell_update(1, 4), 0)

    def test_cell_update_birth(self):
        self.assertEqual(cell_update(0,3), 1)

    def test_cell_update_survive(self):
        self.assertEqual(cell_update(1,2), 1)

    def test_cell_update_underpop(self):
        self.assertEqual(cell_update(1,1),0)


def cell_update(cell, neighbours):
    if neighbours == 3 or neighbours == 2:
        return 1
    else:
        return 0

if __name__ == "__main__":

    unittest.main()
    

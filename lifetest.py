import unittest

class test_cell_updates(unittest.TestCase):
    
    def test_cell_update_overpop(self):
        self.assertEqual(cell_update(1, 4), 0)

    def test_cell_update_birth(self):
        self.assertEqual(cell_update(0,3), 1)

    def test_cell_update(self):
        self.assertEqual(cell_update(1,3), 1)

def cell_update(cell, neighbours):
    if neighbours == 3:
        return 1
    else:
        return 0

if __name__ == "__main__":

    unittest.main()
    

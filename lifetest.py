import unittest

class test_cell_updates(unittest.TestCase):
    
    def test_cell_update_overpop(self):
        self.assertEqual(cell_update(1, 4), 0)

    def test_cell_update_birth(self):
        self.assertEqual(cell_update(0,3), 1)

def cell_update(cell, neighbours):
    if cell == 1:
        return 0
    else:
        return 1

if __name__ == "__main__":

    unittest.main()
    

import unittest

class test_cell_updates(unittest.TestCase):
    
    def test_cell_update_overpop(self):
        assert(cell_update(1, 4), 0)

def cell_update(cell, neighbours):
    return 0

if __name__ == "__main__":

    unittest.main()
    

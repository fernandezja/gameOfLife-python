import unittest
from core.entities.cellule import *
 

class CelluleTest(unittest.TestCase):
    def setUp(self):
        self.cell = Cellule()
        
    def testCelluleShouldInitializeWithName(self):
        expectedResult = 'nameCell1'
        cell = Cellule('nameCell1')
        self.assertEqual(cell.name, expectedResult)

    def testCelluleShouldToStringDescription(self):
        expectedResult = 'Cellule(name=cellule1)'        
        cell = Cellule('cellule1')
        self.assertEqual(cell.toString(), expectedResult)

if __name__ == '__main__':
    unittest.main()

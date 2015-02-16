import unittest
from core.entities.point import *
 

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.punto = Point()

    def setUp(self):
        self.punto = None

    def testPointShouldInitializeInitiaPosition(self):
        punto = Point()
        self.assertEqual(punto.x, 0)
        self.assertEqual(punto.y, 0)

    def testPointShouldInitializeCustomPosition(self):
        punto = Point(137, 138)
        self.assertEqual(punto.x, 137)
        self.assertEqual(punto.y, 138)

    def testPointShouldToStringDescription(self):
        punto = Point(37, 37)
        resultadoEsperado = 'Point(x=37, y=37)'
        self.assertEqual(punto.toString(), resultadoEsperado)

    def testPointShouldKnowIfItIsANeighbourOfAnotherPoint(self):
        punto = Point(10, 10)
        puntoNeighbour = Point(11, 11)
        self.assertTrue(punto.isANeighbour(puntoNeighbour))

    def testPointShouldKnowIfItIsNotANeighbourOfAnotherPoint(self):
        punto = Point(10, 10)
        puntoNotNeighbour = Point(50, 50)
        self.assertFalse(punto.isANeighbour(puntoNotNeighbour))




if __name__ == '__main__':
    unittest.main()

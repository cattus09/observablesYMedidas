import math

import LIbComp as lc
import unittest

class TestCompOperatios(unittest.TestCase):

    def test_sumaComp(self):
        suma = lc.sumaComp((5,-4),(3,-3))
        self.assertAlmostEqual(suma[0],8)
        self.assertAlmostEqual(suma[1],-7)

    def test_restaCom(self):
        resta = lc.restaCom((5,-4),(3,-3))
        self.assertAlmostEqual(resta[0],2)
        self.assertAlmostEqual(resta[1],-1)

    def test_producComp(self):
        producto = lc.producComp((5,-4),(3,-3))
        self.assertAlmostEqual(producto[0],3)
        self.assertAlmostEqual(producto[1],-27)

    def test_divComp(self):
        division = lc.divComp((2,-4),(4,-2))
        self.assertAlmostEqual(division[0],0.8)
        self.assertAlmostEqual(division[1],-0.6)

    def test_modComp(self):
        modulo = lc.modComp((3, 4))
        self.assertAlmostEqual(modulo, 5)


    def test_conjComp(self):
        conjugado = lc.conjComp((5, -4))
        self.assertAlmostEqual(conjugado[0], 5)
        self.assertAlmostEqual(conjugado[1], 4)

    def test_polComp(self):
        polar = lc.polComp((3, 3))
        self.assertAlmostEqual(polar[0], 3*(2**(1/2)))
        self.assertAlmostEqual(polar[1], 0.7853981633974483)

    def test_faseComp(self):
        suma = lc.faseComp((3, 3))
        self.assertAlmostEqual(suma, (1/4)*math.pi)

if __name__ == '__main__':
    unittest.main()


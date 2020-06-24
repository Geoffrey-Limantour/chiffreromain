import unittest
from romanizer import Selector
from romanizer import Transpose

class SelectorTestCase(unittest.TestCase):

    def test_selector1(self):
        resultat = Selector(1)
        self.assertEqual(resultat,"I")
    def test_selector3(self):
        resultat = Selector(3)
        self.assertEqual(resultat,"III")
    def test_selector5(self):
        resultat = Selector(5)
        self.assertEqual(resultat,"V")
    def test_selector8(self):
        resultat = Selector(8)
        self.assertEqual(resultat,"VIII")
    def test_selector9(self):
        resultat = Selector(9)
        self.assertEqual(resultat,"IX")
    def test_selector479(self):
        resultat = Selector(479)
        self.assertEqual(resultat,"CDLXXIX")

    
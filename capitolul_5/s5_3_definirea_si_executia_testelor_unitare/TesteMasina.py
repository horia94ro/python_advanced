from capitolul_5.s5_3_definirea_si_executia_testelor_unitare.Masina import Masina
import unittest


class TesteMasina(unittest.TestCase):

    def setUp(self) -> None:
        self.golf = Masina()

    def test_viteza_initiala(self):
        self.assertEqual(self.golf.viteza_curenta, 0)

    def test_distanta_initiala(self):
        self.assertEqual(self.golf.km_parcursi, 0)

    def test_timp_initial(self):
        self.assertEqual(self.golf.timp_deplasare, 0)

    def test_accelerare_start(self):
        self.golf.accelereaza()
        self.assertGreater(self.golf.viteza_curenta, 0)
        self.assertEqual(self.golf.viteza_curenta, 10)

    def test_franeaza(self):
        self.golf.accelereaza()
        self.golf.franeaza()
        self.assertEqual(self.golf.viteza_curenta, 0)

    def test_accelerare_multipla(self):
        for _ in range(3):
            self.golf.accelereaza()
        self.assertGreater(self.golf.viteza_curenta, 10)
        self.assertEqual(self.golf.viteza_curenta, 30)

    def test_franare_multipla(self):
        for _ in range(3):
            self.golf.franeaza()
        self.assertEqual(self.golf.viteza_curenta, 0)
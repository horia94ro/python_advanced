from capitolul_5.s5_4_suite_de_teste.Motocicleta import Motocicleta
import unittest


class TesteMotocicleta(unittest.TestCase):

    def setUp(self) -> None:
        self.kawsaki = Motocicleta()

    def test_pasageri_initiali(self):
        self.assertEqual(self.kawsaki.nr_pasageri, 2)

    def test_consum_initial(self):
        self.assertEqual(self.kawsaki.consum, 5)

    def test_viteza_initiala(self):
        self.assertEqual(self.kawsaki.viteza_curenta, 15)

    def test_accelarare(self):
        self.kawsaki.accelereaza()
        self.assertEqual(self.kawsaki.viteza_curenta, 30)
        self.assertGreater(self.kawsaki.consum, 5)

    def test_oprire(self):
        self.kawsaki.franeaza()
        self.assertEqual(self.kawsaki.viteza_curenta, 0)
        self.assertEqual(self.kawsaki.consum, 0)
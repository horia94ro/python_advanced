import unittest
from capitolul_5.s5_4_suite_de_teste.TesteMasina import TesteMasina
from capitolul_5.s5_4_suite_de_teste.TesteMotocicleta import TesteMotocicleta

#Definim doua instanțe de TestLoader - câte una pentru fiecare clasă de teste
loader_masina = unittest.TestLoader()
loader_motociclta = unittest.TestLoader()


#Implementăm 3 suite separate; În funcție de necesități, poate să fie rulată doar una dintre acestea

suita_completa = unittest.TestSuite()
suita_completa.addTests(loader_masina.loadTestsFromTestCase(TesteMasina))
suita_completa.addTests(loader_motociclta.loadTestsFromTestCase(TesteMotocicleta))

suita_masina = unittest.TestSuite()
suita_masina.addTests(loader_masina.loadTestsFromTestCase(TesteMasina))

suita_motocicleta = unittest.TestSuite()
suita_motocicleta.addTests(loader_motociclta.loadTestsFromTestCase(TesteMotocicleta))

#În continuare, în funcție de ceea ce ne dorim să rulăm, dăm ca și argument metodei de run() doar suita pe care o vrem rulată
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suita_motocicleta)

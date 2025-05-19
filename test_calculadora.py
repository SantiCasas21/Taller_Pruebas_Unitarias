import unittest
import math
from calculadora import seno, coseno, tangente, inverso_seno, log_base10, factorial, combinatoria
from calculadora import inverso_coseno, inverso_tangente, potencia, log_natural, raiz_cuadrada, raiz_enesima
from calculadora import inverso, pi, seno_hiperbolico, coseno_hiperbolico, tangente_hiperbolica

class TestCalculadora(unittest.TestCase):

    def test_seno(self):
        self.assertAlmostEqual(seno(math.pi/2), 1.0, places=5)

    def test_coseno(self):
        self.assertAlmostEqual(coseno(0), 1.0, places=5)

    def test_tangente(self):
        self.assertAlmostEqual(tangente(0), 0.0, places=5)

    def test_inverso_seno_valido(self):
        self.assertAlmostEqual(inverso_seno(0), 0.0, places=5)

    def test_inverso_seno_invalido(self):
        with self.assertRaises(ValueError):
            inverso_seno(2)

    def test_log_base10_valido(self):
        self.assertAlmostEqual(log_base10(100), 2.0, places=5)

    def test_log_base10_invalido(self):
        with self.assertRaises(ValueError):
            log_base10(-5)

    def test_factorial_valido(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_invalido(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_combinatoria_valida(self):
        self.assertEqual(combinatoria(5, 3), 10)

    def test_combinatoria_invalida(self):
        with self.assertRaises(ValueError):
            combinatoria(3, 5)

    def test_inverso_coseno_valido(self):
        self.assertAlmostEqual(inverso_coseno(1), 0.0, places=5)

    def test_inverso_tangente_valido(self):
        self.assertAlmostEqual(inverso_tangente(0), 0.0, places=5)

    def test_potencia_valida(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_log_natural_valido(self):
        self.assertAlmostEqual(log_natural(math.e), 1.0, places=5)

    def test_raiz_cuadrada_valida(self):
        self.assertAlmostEqual(raiz_cuadrada(4), 2.0, places=5)

    def test_raiz_enesima_valida(self):
        self.assertAlmostEqual(raiz_enesima(27, 3), 3.0, places=5)

    def test_inverso_valido(self):
        self.assertAlmostEqual(inverso(2), 0.5, places=5)

    def test_pi_valido(self):
        self.assertAlmostEqual(pi(), math.pi, places=5)

    def test_seno_hiperbolico_valido(self):
        self.assertAlmostEqual(seno_hiperbolico(0), 0.0, places=5)

    def test_coseno_hiperbolico_valido(self):
        self.assertAlmostEqual(coseno_hiperbolico(0), 1.0, places=5)

    def test_tangente_hiperbolica_valida(self):
        self.assertAlmostEqual(tangente_hiperbolica(0), 0.0, places=5)

if __name__ == '__main__':
    unittest.main(verbosity=2)

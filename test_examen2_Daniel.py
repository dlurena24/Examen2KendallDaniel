import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(5, 120, 12, 
                           ["Canción 1", "Canción 2", "Canción 3"],
                           [0.8, 0.9, 0.7])

    # ------------------------------
    # Pruebas de ObtieneValencia
    # ------------------------------
    def test_obtiene_valencia_valor_normal(self):
        self.assertEqual(self.obj.ObtieneValencia(1234567), 4)

    def test_obtiene_valencia_sin_impares(self):
        self.assertEqual(self.obj.ObtieneValencia(2468), 0)

    # ------------------------------
    # Pruebas de DivisibleTempo
    # ------------------------------
    def test_divisible_tempo_valor_normal(self):
        self.assertEqual(self.obj.DivisibleTempo(10), [1, 2, 5, 10])

    def test_divisible_tempo_primo(self):
        self.assertEqual(self.obj.DivisibleTempo(13), [1, 13])

    # ------------------------------
    # Pruebas de ObtieneMasBailable
    # ------------------------------
    def test_obtiene_mas_bailable_lista_normal(self):
        self.assertEqual(self.obj.ObtieneMasBailable([0.1, 0.5, 0.3]), 0.5)

    def test_obtiene_mas_bailable_lista_vacia(self):
        self.assertIsNone(self.obj.ObtieneMasBailable([]))

    # ------------------------------
    # Pruebas de VerificaListaCanciones
    # ------------------------------
    def test_verifica_lista_canciones_valida(self):
        self.assertTrue(self.obj.VerificaListaCanciones(["A", "B", "C"]))

    def test_verifica_lista_canciones_con_none(self):
        self.assertFalse(self.obj.VerificaListaCanciones(["A", None, "C"]))


if __name__ == "__main__":
    unittest.main()

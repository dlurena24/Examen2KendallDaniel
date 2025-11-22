from Examen2 import MiClase
import unittest

class TestMiClase(unittest.TestCase):
    def setUp(self):
        # Se crea una instancia que se reutiliza en las pruebas
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    # ObtieneValencia
    def test_ObtieneValencia_caso_cero(self):
        self.assertEqual(self.objeto.ObtieneValencia(0), 0)  # Cero no es impar

    def test_ObtieneValencia_caso_mixto(self):
        self.assertEqual(self.objeto.ObtieneValencia(8), 0)  # Ocho no es impar
        self.assertEqual(self.objeto.ObtieneValencia(7), 1)  # Siete sí es impar
        
    # DivisibleTempo
    def test_DivisibleTempo_divisores_8(self):
        self.assertEqual(self.objeto.DivisibleTempo(8), [1, 2, 4, 8])  # Divisores de 8

    def test_DivisibleTempo_divisores_1(self):
        self.assertEqual(self.objeto.DivisibleTempo(1), [1])  # Solo 1 es divisor de sí mismo

    # ObtieneMasBailable
    def test_ObtieneMasBailable_lista_numeros_positivos_negativos(self):
        self.assertEqual(self.objeto.ObtieneMasBailable([-1, 0, 1]), 1)  # Mezcla de negativos y positivos

    def test_ObtieneMasBailable_lista_repetidos(self):
        self.assertEqual(self.objeto.ObtieneMasBailable([5, 2, 5, 3]), 5)  # Repetidos valores máximos

    # VerificaListaCanciones
    def test_VerificaListaCanciones_todo_none(self):
        self.assertFalse(self.objeto.VerificaListaCanciones([None, None]))  # Todos son None

    def test_VerificaListaCanciones_vacia(self):
        self.assertTrue(self.objeto.VerificaListaCanciones([]))  # Lista vacía es válida (no contiene None)

    def test_encuentra_elemento_presente(self):
        self.assertTrue(self.objeto.Encuentra([1, 2, 3, 4], 30000))  # 3 sí está en la lista

    def test_encuentra_elemento_ausente(self):
        self.assertFalse(self.objeto.Encuentra([1, 2, 3, 4], 5))  # 5 no está en la lista



if __name__ == "__main__":
    unittest.main()

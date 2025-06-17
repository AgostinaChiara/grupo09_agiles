"""
Archivo de pruebas unitarias para la clase Ahorcado.

Este archivo contiene tests automáticos que validan el comportamiento
del juego del Ahorcado, incluyendo:
- Aciertos e intentos fallidos de letras.
- Adivinanza de palabras completas.
- Control del estado del juego (victoria, derrota).
- Visualización de la palabra parcial.
- Manejo de entradas en mayúsculas y minúsculas.
"""
# tests/test_ahorcado.py
# pylint: disable=wrong-import-position

import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ahorcado import Ahorcado

class TestAhorcado(unittest.TestCase):
    """Tests unitarios para la clase Ahorcado."""
    def test_arriesgar_palabra_correcta(self):
        """Verifica que adivinar correctamente la palabra finaliza el juego con victoria."""
        juego = Ahorcado(2)
        secreta = juego.palabra_secreta
        self.assertEqual(juego.arriesgar_palabra(secreta),True)

    def test_adivinar_palabra_incorrecta(self):
        """Verifica que adivinar incorrectamente una palabra
        reduce los intentos y no da victoria.
        """
        juego = Ahorcado(3, intentos_maximos=3)
        resultado = juego.arriesgar_palabra("pasapalabra")
        self.assertFalse(resultado)
        self.assertFalse(juego.victoria)
        self.assertTrue(juego.juego_terminado)

    def test_adivinar_letra_correcta(self):
        """Verifica el comportamiento al adivinar una letra correcta."""
        juego = Ahorcado(2)
        secreta = juego.palabra_secreta
        resultado = juego.arriesgar_letra(secreta[0])

        #Verifica que la letra este en la palabra.
        self.assertTrue(resultado)

        #Verificar que no bajo la cantidad de intentos.
        self.assertEqual(juego.intentos_restantes, 6)
        self.assertNotEqual(juego.intentos_restantes, 5)

        #Verifica que la letra este dentro de las letras adivinadas.
        self.assertIn(secreta[0], juego.letras_adivinadas)

    def test_adivinar_letra_incorrecta(self):
        """Verifica el comportamiento al adivinar una letra incorrecta."""
        juego = Ahorcado(2)
        secreta = juego.palabra_secreta
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        letra_incorrecta = None

        for letra in alfabeto:
            if letra not in secreta:
                letra_incorrecta = letra
                break
        resultado = juego.arriesgar_letra(letra_incorrecta)

        #Verifica que la letra no este en la palabra.
        self.assertFalse(resultado)

        #Verificar que bajo la cantidad de intentos.
        self.assertEqual(juego.intentos_restantes, 5)
        self.assertNotEqual(juego.intentos_restantes, 6)

        #Verifica que la letra este dentro de las letras adivinadas.
        self.assertIn(letra_incorrecta, juego.letras_adivinadas)

    def test_derrota_sin_intentos(self):
        """Simula una derrota por quedarse sin intentos luego de varias letras incorrectas."""
        juego = Ahorcado(2, intentos_maximos=2)

        secreta = juego.palabra_secreta
        alfabeto = "abcdefghijklmnopqrstuvwxyz"
        letras_incorrectas = list()

        for letra in alfabeto:
            if letra not in secreta:
                letras_incorrectas.append(letra)

        #Se intenta la primer letra incorrecta
        juego.arriesgar_letra(letras_incorrectas[0])

        #Verificar que el juego no termine en victoria.
        self.assertFalse(juego.victoria)
        #Verificar que le queda un intento mas.
        self.assertEqual(juego.intentos_restantes, 1)
        #Verificar que el juego no termino.
        self.assertFalse(juego.juego_terminado)

        #Se intenta la segunda letra incorrecta
        juego.arriesgar_letra(letras_incorrectas[1])

        #Verificar que el juego no termine en victoria.
        self.assertFalse(juego.victoria)
        #Verificar que no le quedan mas intentos.
        self.assertEqual(juego.intentos_restantes, 0)
        #Verificar que el juego termino
        self.assertTrue(juego.juego_terminado)

    def test_palabra_actual_inicio(self):
        """Verifica que al inicio, la palabra actual solo muestra guiones bajos."""
        juego = Ahorcado(3)
        secreta = juego.palabra_secreta
        #Verificar que tenga misma cantidad de letras.
        actual = "_ " * len(secreta)
        p_actual = juego.palabra_actual()
        self.assertEqual(p_actual, actual[:-1])

    # def test_palabra_actual_inicio(self):
    #     """Verifica que al inicio, la palabra actual solo muestra guiones bajos."""
    #     juego = Ahorcado(3)
    #     secreta = juego.palabra_secreta
    #     actual = juego.palabra_actual()
    #     guiones_esperados = "_ " * len(secreta)
    #     guiones_esperados = guiones_esperados.strip()
            
    #     print("Secreta:", secreta)
    #     print("Palabra actual:", actual)
            
    #     self.assertEqual(actual, guiones_esperados)


    # def test_palabra_actual_con_letras_adivinadas(self):
    #     """Verifica que la palabra actual refleje correctamente las letras adivinadas."""
    #     juego = Ahorcado("hola")
    #     #Se arriesga la primer letra para ver si se encuentra en la palabra
    #     juego.arriesgar_letra("h")

    #     #Verifica que la funcion palabra actual devuelva las letras adivinadas en su orden correcto
    #     self.assertEqual(juego.palabra_actual(), "h _ _ _")
    #     self.assertNotEqual(juego.palabra_actual(), "_ h _ _")
    #     self.assertNotEqual(juego.palabra_actual(), "h _ h _")

    #     #Se arriesga la ultima letra para ver si se encuentra en la palabra
    #     juego.arriesgar_letra("a")

    #     #Verifica que la funcion palabra actual devuelva las letras adivinadas en su orden correcto
    #     self.assertEqual(juego.palabra_actual(), "h _ _ a")
    #     self.assertNotEqual(juego.palabra_actual(), "_ _ _ a")
    #     self.assertNotEqual(juego.palabra_actual(), "h _ _ _")

    # def test_palabra_en_mayusculas_se_convierte_a_minusculas(self):
    #     """Test que la palabra se convierte a minúsculas"""
    #     juego = Ahorcado("PYTHON")
    #     #Verifica que la palabra secreta se convierta a minúscula
    #     self.assertEqual(juego.palabra_secreta, "python")
    #     #Verifica que la palabra secreta no siga en mayúscula
    #     self.assertNotEqual(juego.palabra_secreta, "PYTHON")

    # def test_no_se_puede_continuar_despues_de_ganar(self):
    #     """Verifica que no se pueda seguir jugando después de ganar el juego."""
    #     juego = Ahorcado("python")
    #     juego.arriesgar_palabra("python")
    #     self.assertTrue(juego.juego_terminado)
    #     self.assertTrue(juego.victoria)

    #     #No se puede jugar luego de ganar
    #     self.assertFalse(juego.arriesgar_letra("p"))

    # def test_ganar_adivinando_todas_las_letras(self):
    #     """
    #     Verifica que el juego termine con victoria al adivinar todas las letras
    #     correctamente una por una, sin arriesgar la palabra completa.
    #     """
    #     juego = Ahorcado("sol")

    #     # Adivinar todas las letras correctamente, una por una
    #     juego.arriesgar_letra("s")
    #     juego.arriesgar_letra("o")
    #     juego.arriesgar_letra("l")

    #     # Verificar que se ejecutó la lógica de victoria
    #     self.assertTrue(juego.juego_terminado)
    #     self.assertTrue(juego.victoria)

    # def test_palabra_actual_con_letras_repetidas(self):
    #     '''
    #     Verificar que la palabra actual no muestre
    #     letras que no hayan sido adivinadas aún
    #     '''
    #     juego = Ahorcado("banana")
    #     juego.arriesgar_letra("a")
    #     # La 'a' aparece 3 veces y debería mostrarlas todas
    #     self.assertEqual(juego.palabra_actual(), "_ a _ a _ a")

if __name__ == "__main__":
    unittest.main() # pragma: no cover

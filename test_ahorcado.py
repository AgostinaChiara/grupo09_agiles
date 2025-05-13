import unittest
from ahorcado import Ahorcado

class TestAhorcado(unittest.TestCase):
  def test_arriesgar_palabra_correcta(self):
    juego = Ahorcado("ahorcado")
    self.assertEqual(juego.arriesgar_palabra("ahorcado"),True)
  
  # def test_adivinar_palabra_correcta(self):
  #   juego = Ahorcado("ahorcado")
  #   resultado = juego.arriesgar_palabra("ahorcado")
  #   self.assertTrue(resultado)
  #   self.assertTrue(juego.juego_terminado)
  #   self.assertTrue(juego.victoria)

  def test_adivinar_palabra_incorrecta(self):
    juego = Ahorcado("ahorcado", intentos_maximos=1)
    resultado = juego.arriesgar_palabra("pasapalabra")
    self.assertFalse(resultado)

  # def test_adivinar_letra_correcta(self):
  #   juego = Ahorcado("python")
  #   resultado = juego.adivinar_letra("p")
  #   self.assertTrue(resultado)
  #   self.assertEqual(juego.intentos_restantes, 6) 
  #   self.assertIn("p", juego.letras_adivinadas)
    
  # def test_adivinar_letra_incorrecta(self):
  #   juego = Ahorcado("python")
  #   resultado = juego.adivinar_letra("a")
  #   self.assertFalse(resultado)
  #   self.assertEqual(juego.intentos_restantes, 5)
  #   self.assertIn("a", juego.letras_adivinadas)

if __name__ == "__main__":
  unittest.main()
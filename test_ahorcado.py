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

  def test_adivinar_letra_correcta(self):
    juego = Ahorcado("python")
    resultado = juego.arriesgar_letra("p")
    
    #Verifica que la letra este en la palabra.
    self.assertTrue(resultado)
    
    #Verificar que no bajo la cantidad de intentos.
    self.assertEqual(juego.intentos_restantes, 6) 
    self.assertNotEqual(juego.intentos_restantes, 5)
    
    #Verifica que la letra este dentro de las letras adivinadas.
    self.assertIn("p", juego.letras_adivinadas)


  def test_adivinar_letra_incorrecta(self):
    juego = Ahorcado("python")
    resultado = juego.arriesgar_letra("a")

    #Verifica que la letra no este en la palabra.
    self.assertFalse(resultado)
    
    #Verificar que bajo la cantidad de intentos.
    self.assertEqual(juego.intentos_restantes, 5)
    self.assertNotEqual(juego.intentos_restantes, 6)

    #Verifica que la letra este dentro de las letras adivinadas.
    self.assertIn("a", juego.letras_adivinadas)

  def test_derrota_sin_intentos(self):
    juego = Ahorcado("sol", intentos_maximos=2)

    #Se intenta la primer letra incorrecta 
    juego.arriesgar_letra("x")

    #Verificar que el juego no termine en victoria.
    self.assertFalse(juego.victoria)
    #Verificar que le queda un intento mas.
    self.assertEqual(juego.intentos_restantes, 1)
    #Verificar que el juego no termino.
    self.assertFalse(juego.juego_terminado)

    #Se intenta la segunda letra incorrecta
    juego.arriesgar_letra("y")

    #Verificar que el juego no termine en victoria.
    self.assertFalse(juego.victoria)
    #Verificar que no le quedan mas intentos.
    self.assertEqual(juego.intentos_restantes, 0)
    #Verificar que el juego termino
    self.assertTrue(juego.juego_terminado)

  # def test_palabra_actual_inicio(self):
  #   juego = Ahorcado("hola")
  #   self.assertEqual(juego.palabra_actual(), "____")



if __name__ == "__main__":
  unittest.main()
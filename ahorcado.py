class Ahorcado:
  def __init__(self, palabra, intentos_maximos=6):
    self.palabra_secreta = palabra.lower()
    self.intentos_maximos = intentos_maximos
    self.intentos_restantes = intentos_maximos
    self.letras_adivinadas = set()
    self.juego_terminado = False
    self.victoria = False

  def arriesgar_letra(self, letra):
    letra = letra.lower()

    self.letras_adivinadas.add(letra)

    if letra in self.palabra_secreta:
      self._verificar_victoria()
      return True
    else:
      self.intentos_restantes -= 1
        
      if self.intentos_restantes <= 0:
        self.juego_terminado = True
      
      return False
    
  def arriesgar_palabra(self, palabra_intento):
    palabra_intento = palabra_intento.lower()
    
    if palabra_intento == self.palabra_secreta:
      self.juego_terminado = True
      self.victoria = True
      return True
    else:
      self.intentos_restantes -= 1
      
      if self.intentos_restantes <= 0:
        self.juego_terminado = True
      
      return False  
    
  def _verificar_victoria(self):
    for letra in self.palabra_secreta:
      if letra not in self.letras_adivinadas:
        return
    
    self.juego_terminado = True
    self.victoria = True

  def palabra_actual(self):
    resultado = ""
    for letra in self.palabra_secreta:
      if letra in self.letras_adivinadas:
        resultado += letra
      else:
        resultado += "_"
    return resultado
  
  
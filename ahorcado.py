'''
Archivo .py para el TPI de la materia Metodologias Agiles  
'''

class Ahorcado:
    '''
    Clase que representa el juego del Ahorcado.

    Administra el estado del juego, las letras adivinadas,
    y verifica condiciones de victoria o derrota.
    '''
    def __init__(self, palabra, intentos_maximos=6):
        '''
        Inicializa el juego del ahorcado con la palabra secreta y los intentos máximos.

        :param palabra: Palabra a adivinar.
        :param intentos_maximos: Cantidad máxima de intentos permitidos.
        '''
        self.palabra_secreta = palabra.lower()
        self.intentos_maximos = intentos_maximos
        self.intentos_restantes = intentos_maximos
        self.letras_adivinadas = set()
        self.juego_terminado = False
        self.victoria = False

    def arriesgar_letra(self, letra):
        '''
        Intenta adivinar una letra de la palabra secreta.

        :param letra: Letra que el jugador quiere adivinar.
        :return: True si la letra está en la palabra, False en caso contrario.
        '''
        letra = letra.lower()
        self.letras_adivinadas.add(letra)
        if self.juego_terminado:
            return False
        if letra in self.palabra_secreta:
            self._verificar_victoria()
            return True

        self.intentos_restantes -= 1

        if self.intentos_restantes <= 0:
            self.juego_terminado = True

        return False

    def arriesgar_palabra(self, palabra_intento):
        '''
        Intenta adivinar toda la palabra secreta.

        :param palabra_intento: Palabra que el jugador intenta adivinar.
        :return: True si la palabra es correcta, False en caso contrario.
        '''
        palabra_intento = palabra_intento.lower()

        if palabra_intento == self.palabra_secreta:
            self.juego_terminado = True
            self.victoria = True
            return True
        self.intentos_restantes -= 1

        if self.intentos_restantes <= 0:
            self.juego_terminado = True

            return False

    def _verificar_victoria(self):
        '''
        Verifica si el jugador ha adivinado todas las letras de la palabra secreta.
        '''
        for letra in self.palabra_secreta:
            if letra not in self.letras_adivinadas:
                return

        self.juego_terminado = True
        self.victoria = True

    def palabra_actual(self):
        '''
        Muestra el estado actual de la palabra con las letras adivinadas hasta el momento.

        :return: Cadena con letras adivinadas y guiones bajos por letras faltantes.
        '''
        resultado = ""
        for letra in self.palabra_secreta:
            if letra in self.letras_adivinadas:
                resultado += letra + " "
            else:
                resultado += "_ "
        resultado = resultado[:-1]
        return resultado
  
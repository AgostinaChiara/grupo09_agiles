Feature: Partida del juego del Ahorcado

  Scenario: Al comenzar el juego, la palabra debe estar oculta
    Given el jugador inicia una nueva partida
    Then debería ver la palabra oculta como guiones bajos

  Scenario: El jugador adivina una letra incorrecta
    Given el jugador inicia una nueva partida
    When el jugador ingresa una letra que no está en la palabra
    Then el contador de errores debería incrementarse

  Scenario: El jugador pierde el juego tras 6 errores
    Given el jugador inicia una nueva partida
    When el jugador ingresa 6 letras incorrectas
    Then el jugador debería ver el mensaje de derrota

  Scenario: El botón de una letra usada se desactiva
    Given el jugador inicia una nueva partida
    When el jugador hace clic en una letra
    Then el botón de esa letra debería estar desactivado

  Scenario: Ganar completando letras una a una
    Given el jugador inicia una nueva partida
    When el jugador presiona todas las letras correctas de la palabra
    Then el jugador debería ver el mensaje de victoria
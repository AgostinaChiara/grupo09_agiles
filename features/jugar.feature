Feature: Partida del juego del Ahorcado

  Scenario: El jugador ingresa solo letras incorrectas y pierde
    Given el jugador inicia una nueva partida
    When ingresa 6 letras que no están en la palabra
    Then el jugador pierde la partida

  Scenario: El jugador ingresa solo letras correctas y gana
    Given el jugador inicia una nueva partida
    When ingresa 6 letras que están en la palabra
    Then el jugador gana la partida

  Scenario: El jugador ingresa letras correctas e incorrectas y gana
    Given el jugador inicia una nueva partida
    When ingresa 1 letra correcta 2 incorrectas 1 correcta 2 incorrectas y el resto de las correctas 
    Then el jugador gana la partida

  Scenario: El jugador ingresa letras correctas e incorrectas y pierde
    Given el jugador inicia una nueva partida
    When ingresa 1 letra incorrecta 1 correcta 1 incorrecta 1 correcta 4 incorrectas
    Then el jugador pierde la partida
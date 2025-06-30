Feature: Selección de dificultad en el juego del ahorcado

    Scenario: Seleccionar dificultad facil y redirigir al juego
        Given el usuario está en la página principal del ahorcado
        When el usuario selecciona la dificultad "facil"
        Then el usuario debería ver la dificultad "facil" en pantalla

    Scenario: Seleccionar dificultad medio y redirigir al juego
        Given el usuario está en la página principal del ahorcado
        When el usuario selecciona la dificultad "medio"
        Then el usuario debería ver la dificultad "medio" en pantalla

    Scenario: Seleccionar dificultad dificil y redirigir al juego
        Given el usuario está en la página principal del ahorcado
        When el usuario selecciona la dificultad "dificil"
        Then el usuario debería ver la dificultad "dificil" en pantalla
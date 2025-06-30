function elegirDificultad(dificultad) {

    // Guardamos la dificultad elegida
    localStorage.setItem('dificultadAhorcado', dificultad);    
    window.open("/juego", "_self");
}

// Efectos interactivos para cuando carga la pagina
window.addEventListener('load', function() {
const buttons = document.querySelectorAll('.btn-dificultad');
buttons.forEach((button, index) => {
    setTimeout(() => {
            button.style.animation = 'pulse 0.6s ease-in-out';
        }, index * 200);
    });
});
// Estado juego
let palabraActual = 'ABC';
let letrasAdivinadas = [];
let errores = 0;
let erroresMaximos = 6;
let juegoTerminado = false;
let dificultad = 'medio';
let idJuego = null;


// Hangman parts to show on wrong guesses
const partesAhorcado = ['head', 'body', 'leftArm', 'rightArm', 'leftLeg', 'rightLeg'];

// Inicializar juego
function iniciarJuego() {
  // Obtener dificulrad del localStorage, si no tiene que sea medio
  dificultad = localStorage.getItem('dificultadAhorcado') || 'medio';

  erroresMaximos = 6
  
  // Update UI
  actualizarMostrarDificultad();
  crearTeclado();
  juegoNuevo();
}

function actualizarMostrarDificultad() {
  const badge = document.getElementById('dificultadElegida');
  badge.textContent = dificultad.charAt(0).toUpperCase() + dificultad.slice(1);
  badge.className = `dificultad-elegida dificultad-${dificultad}`;
  
  document.getElementById('intentosRestantes').textContent = erroresMaximos;
}

function crearTeclado() {
  const grid = document.getElementById('gridTeclado');
  const alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  
  grid.innerHTML = '';
  for (let letra of alfabeto) {
    const button = document.createElement('button');
    button.className = 'letra-btn';
    button.textContent = letra;
    button.onclick = () => adivinarLetra(letra);
    button.id = `btn-${letra}`;
    grid.appendChild(button);
  }
}

function volverInicio() {
  window.open('/','_self')
}

async function adivinarLetra(letra) {
  if (juegoTerminado || letrasAdivinadas.includes(letra)) return;

  letrasAdivinadas.push(letra);

  const res = await fetch('/juego/letra', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({letra, idJuego})
  });

  const data = await res.json();
  palabraActual = data.palabraActual.replace(/ /g, '');
  errores = data.errores;
  juegoTerminado = data.terminado;

  const button = document.getElementById(`btn-${letra}`);
  button.classList.add(data.letraCorrecta ? 'correct' : 'incorrect');
  button.disabled = true;

  document.getElementById("cantErrores").textContent = errores;
  document.getElementById("intentosRestantes").textContent = data.intentosRestantes;
  actualizarPalabraActual();
  actualizarAhorcado();

  if (juegoTerminado) {
    const msg = data.victoria ? "¡Ganaste! 🎉" : `¡Perdiste! 😞 La palabra era: ${data.secreta}`;
    const msjeJuego = document.getElementById("mensajeJuego"); 
    msjeJuego.textContent = msg;
    msjeJuego.className = `mensaje-juego ${data.victoria ? 'win' : 'lose'} show`;
  }
}

async function juegoNuevo() {
  const res = await fetch('/juego/nuevo', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ dificultad })
  });
  const data = await res.json();

  palabraActual = data.palabraActual.replace(/ /g, '');
  letrasAdivinadas = [];
  errores = data.errores;
  erroresMaximos = data.intentosRestantes + data.errores;
  juegoTerminado = false;
  idJuego = data.idJuego;


  actualizarMostrarDificultad();
  crearTeclado();
  actualizarPalabraActual();
  document.getElementById("cantErrores").textContent = errores;
  document.getElementById("intentosRestantes").textContent = data.intentosRestantes;
  document.getElementById("mensajeJuego").className = "mensaje-juego";
  document.getElementById("palabra-secreta").textContent = data.palabra_secreta;
  resetearAhorcado();
}

function actualizarPalabraActual() {
    const mostrar = document.getElementById('mostrarPalabra');
    mostrar.innerHTML = '';
    
    for (let letra of palabraActual) {
        const letraBox = document.createElement('div');
        letraBox.className = 'letra-box';
        letraBox.textContent = letra==='_' ? '' : letra.toUpperCase();
        mostrar.appendChild(letraBox);
    }
}

// Resetea el dibujo del ahorcado
function resetearAhorcado() {
  partesAhorcado.forEach(partId => {
    document.getElementById(partId).style.display = 'none';
  });
}

function actualizarAhorcado() {
  if (errores > 0 && errores <= partesAhorcado.length) {
    const parte = document.getElementById(partesAhorcado[errores - 1]);
    parte.style.display = 'block';
  }
}

// Agrega la funcionalidad de escribir las letras por teclado
document.addEventListener('keydown', function(event) {
  const letra = event.key.toUpperCase();
  if (letra >= 'A' && letra <= 'Z') {
    adivinarLetra(letra);
  }
});

// Inicializa el juego cuando se abre la pagina
window.addEventListener('load', iniciarJuego);
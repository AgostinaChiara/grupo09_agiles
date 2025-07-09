from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import tempfile
from dotenv import load_dotenv

LETRAS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
load_dotenv()

TEST_SECRET = os.getenv("TEST_SECRET")



@given('el jugador está en la pantalla de inicio')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get(f"http://localhost:5000/juego?test={TEST_SECRET}")
    time.sleep(1)

@when('selecciona la dificultad "{dificultad}"')
def step_impl(context, dificultad):
    btn = context.driver.find_element(By.ID, f'btn-{dificultad}')
    btn.click()
    time.sleep(1)

@then('debería ver la página del juego cargada')
def step_impl(context):
    assert "juego" in context.driver.current_url
    assert context.driver.find_element(By.ID, "gridTeclado")

@given('el jugador inicia una nueva partida')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(f"http://localhost:5000/juego?test={TEST_SECRET}")
    time.sleep(3)

@then('debería ver la palabra oculta como guiones bajos')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letra_incorrecta = [l for l in LETRAS if l not in palabra][:1]

    boxes = context.driver.find_elements(By.CLASS_NAME, 'letra-box')
    assert len(boxes) > 0
    for box in boxes:
        assert box.text == ''

@when('el jugador ingresa una letra que no está en la palabra')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letra_incorrecta = next((l for l in LETRAS if l not in palabra), None)
    context.driver.find_element(By.ID, f"btn-{letra_incorrecta}").click()
    time.sleep(1)

@then('el contador de errores debería incrementarse')
def step_impl(context):
    errores = context.driver.find_element(By.ID, "cantErrores").text
    assert errores == "1"

@when('el jugador ingresa 6 letras incorrectas')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letras_incorrectas = [l for l in LETRAS if l not in palabra][:6]

    for letra in letras_incorrectas:
        print(letra)
        context.driver.find_element(By.ID, f"btn-{letra}").click()
        time.sleep(0.5)

@then('el jugador debería ver el mensaje de derrota')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    msje = wait.until(EC.visibility_of_element_located((By.ID, "mensajeJuego")))
    msg = msje.text
    assert "¡Perdiste!" in msg, f"Mensaje recibido: {msg}"

@then('el jugador debería ver el mensaje de victoria')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    msje = wait.until(EC.visibility_of_element_located((By.ID, "mensajeJuego")))
    msg = msje.text
    assert "¡Ganaste!" in msg, f"Mensaje recibido: {msg}"

@when('el jugador hace clic en una letra')
def step_impl(context):
    context.letra_usada = 'T'
    context.driver.find_element(By.ID, f'btn-{context.letra_usada}').click()
    time.sleep(1)

@then('el botón de esa letra debería estar desactivado')
def step_impl(context):
    boton = context.driver.find_element(By.ID, f'btn-{context.letra_usada}')
    assert boton.get_attribute("disabled") == "true"

@when('el jugador presiona todas las letras correctas de la palabra')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letras_unicas = sorted(set(palabra))
    for letra in letras_unicas:
        btn = context.driver.find_element(By.ID, f"btn-{letra}")
        btn.click()
        time.sleep(0.3)
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import tempfile
from dotenv import load_dotenv

LETRAS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
load_dotenv()
TEST_SECRET = os.getenv("TEST_SECRET")

def crear_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    return webdriver.Chrome(options=chrome_options)

@given('el jugador inicia una nueva partida')
def step_impl(context):
    context.driver = crear_driver()
    context.driver.get(f"http://localhost:5000/juego?test={TEST_SECRET}")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'letra-box'))
    )

@then('debería ver la palabra oculta como guiones bajos')
def step_impl(context):
    boxes = context.driver.find_elements(By.CLASS_NAME, 'letra-box')
    assert len(boxes) > 0
    for box in boxes:
        assert box.text.strip() == ''

@when('el jugador ingresa una letra que no está en la palabra')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letra_incorrecta = next(l for l in LETRAS if l not in palabra)
    boton = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.ID, f"btn-{letra_incorrecta}"))
    )
    boton.click()
    WebDriverWait(context.driver, 10).until(
        lambda d: d.find_element(By.ID, "cantErrores").text.strip() == "1"
    )

@then('el contador de errores debería incrementarse')
def step_impl(context):
    errores = context.driver.find_element(By.ID, "cantErrores").text.strip()
    assert errores == "1"

@when('el jugador ingresa 6 letras incorrectas')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letras_incorrectas = [l for l in LETRAS if l not in palabra][:6]
    for letra in letras_incorrectas:
        boton = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.ID, f"btn-{letra}"))
        )
        boton.click()
        WebDriverWait(context.driver, 5).until(
            lambda d: d.find_element(By.ID, f"btn-{letra}").get_attribute("disabled") == "true"
        )

@then('el jugador debería ver el mensaje de derrota')
def step_impl(context):
    mensaje = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mensajeJuego"))
    )
    assert "¡Ganaste!" in mensaje.text

@then('el jugador debería ver el mensaje de victoria')
def step_impl(context):
    mensaje = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mensajeJuego"))
    )
    assert "¡Perdiste!" in mensaje.text

@when('el jugador hace clic en una letra')
def step_impl(context):
    context.letra_usada = 'T'
    boton = WebDriverWait(context.driver, 5).until(
        EC.element_to_be_clickable((By.ID, f"btn-{context.letra_usada}"))
    )
    boton.click()
    WebDriverWait(context.driver, 5).until(
        lambda d: d.find_element(By.ID, f"btn-{context.letra_usada}").get_attribute("disabled") == "true"
    )

@then('el botón de esa letra debería estar desactivado')
def step_impl(context):
    boton = context.driver.find_element(By.ID, f'btn-{context.letra_usada}')
    assert boton.get_attribute("disabled") == "true"

@when('el jugador presiona todas las letras correctas de la palabra')
def step_impl(context):
    palabra = context.driver.find_element(By.ID, "palabra-secreta").get_attribute("textContent").strip().upper()
    letras_unicas = sorted(set(palabra))
    for letra in letras_unicas:
        boton = WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.ID, f"btn-{letra}"))
        )
        boton.click()
        WebDriverWait(context.driver, 5).until(
            lambda d: d.find_element(By.ID, f"btn-{letra}").get_attribute("disabled") == "true"
        )

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

LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
load_dotenv()

TEST_SECRET = os.getenv("TEST_SECRET")

@given('el jugador inicia una nueva partida')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get(f"http://localhost:5000/juego?test={TEST_SECRET}")
    time.sleep(1)

@when('ingresa 6 letras que están en la palabra')
def step_impl(context):
    secreta = context.driver.find_element(By.ID, "palabra-secreta").text.upper()
    estan = set(secreta)
    for l in estan:
        btn = context.driver.find_element(By.ID, f"btn-{l}")
        btn.click()
        time.sleep(1)

@when('ingresa 6 letras que no están en la palabra')
def step_impl(context):
    secreta = context.driver.find_element(By.ID, "palabra-secreta").text.upper()
    estan = set(secreta)
    no_estan = list()
    pos = 0
    while len(no_estan)<6:
        if LETRAS[pos] not in estan:
            no_estan.append(LETRAS[pos])
        pos+=1

    for l in no_estan:
        btn = context.driver.find_element(By.ID,f"btn-{l}")
        btn.click()
        time.sleep(1)

@when('ingresa 1 letra correcta 2 incorrectas 1 correcta 2 incorrectas y el resto de las correctas')
def step_impl(context):
    secreta = context.driver.find_element(By.ID, "palabra-secreta").text.upper()
    estan = list(set(secreta))
    no_estan = list()
    pos = 0
    while len(no_estan)<4:
        if LETRAS[pos] not in estan:
            no_estan.append(LETRAS[pos])
        pos+=1
    orden = list()
    orden.append(estan[0])
    orden.extend(no_estan[0:2])
    orden.append(estan[1])
    orden.extend(no_estan[2:4])
    orden.extend(estan[2:])
    
    for l in orden:
        btn = context.driver.find_element(By.ID,f"btn-{l}")
        btn.click()
        time.sleep(1)

@when('ingresa 1 letra incorrecta 1 correcta 1 incorrecta 1 correcta 4 incorrectas')
def step_impl(context):
    secreta = context.driver.find_element(By.ID, "palabra-secreta").text.upper()
    estan = list(set(secreta))
    no_estan = list()
    pos = 0
    while len(no_estan)<6:
        if LETRAS[pos] not in estan:
            no_estan.append(LETRAS[pos])
        pos+=1
    orden = list()
    orden.append(no_estan[0])
    orden.append(estan[0])
    orden.append(no_estan[1])
    orden.extend(estan[1])
    orden.extend(no_estan[2:])
    
    for l in orden:
        btn = context.driver.find_element(By.ID,f"btn-{l}")
        btn.click()
        time.sleep(1)

@then('el jugador pierde la partida')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'mensajeJuego'), '¡Perdiste!')
    )
    badge = context.driver.find_element(By.ID, 'mensajeJuego')
    texto = badge.text
    assert '¡Perdiste!' in texto

@then('el jugador gana la partida')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'mensajeJuego'), '¡Perdiste!')
    )
    badge = context.driver.find_element(By.ID, 'mensajeJuego')
    texto = badge.text
    assert '¡Ganaste!' in texto

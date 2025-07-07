from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import tempfile

@given('el usuario está en la página principal del ahorcado')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("http://localhost:5000/")
    time.sleep(1)

@when('el usuario selecciona la dificultad "{nivel}"')
def step_impl(context, nivel):
    boton = context.driver.find_element(By.CLASS_NAME, nivel)
    boton.click()
    time.sleep(1)

@then('el usuario debería ver la dificultad "{nivel}" en pantalla')
def step_impl(context, nivel):
    badge = context.driver.find_element(By.ID, 'dificultadElegida')
    texto = badge.text
    assert texto.lower() == nivel.lower()

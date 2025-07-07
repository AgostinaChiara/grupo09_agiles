from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import tempfile

@given('el usuario está en la página principal del ahorcado')
def step_impl(context):
    options = Options()
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
    context.driver = webdriver.Chrome(options=options)
    context.driver.get("http://localhost:5000")  # Asegurate que sea la URL correcta
    time.sleep(1)

@when('el usuario selecciona la dificultad "{nivel}"')
def step_impl(context, nivel):
    btn = context.driver.find_element(By.ID, f"btn-{dificultad.lower()}")
    btn.click()
    time.sleep(1)

@then('el usuario debería ver la dificultad "{nivel}" en pantalla')
def step_impl(context, dificultad):
    dificultad_actual = context.driver.find_element(By.ID, "dificultad-actual").text.lower()
    assert dificultad.lower() in dificultad_actual
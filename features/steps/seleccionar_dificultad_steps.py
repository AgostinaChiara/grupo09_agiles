from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('el usuario está en la página principal del ahorcado')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:5000/")  # cambia si usás otro nombre
    time.sleep(1)

@when('el usuario selecciona la dificultad "{nivel}"')
def step_impl(context, nivel):
    boton = context.driver.find_element(By.CLASS_NAME, nivel)
    boton.click()
    time.sleep(1)

@then('el usuario debería ver la dificultad "{nivel}" en pantalla')
def step_impl(context, nivel):
    texto = context.driver.find_element(By.ID, "nivel").text
    assert texto == nivel
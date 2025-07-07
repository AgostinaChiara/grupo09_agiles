from selenium import webdriver
import tempfile
import os
import signal
import psutil

def before_all(context):
    # Configurar el WebDriver antes de todas las pruebas
    options = webdriver.ChromeOptions()
    user_data_dir = tempfile.mkdtemp()  # Crear un directorio temporal único
    options.add_argument(f'--user-data-dir={user_data_dir}')
    options.add_argument('--headless')  # Ejecutar en modo headless si es necesario
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    # Cerrar el WebDriver después de todas las pruebas
    if hasattr(context, 'driver'):
        context.driver.quit()
        # Asegurarse de que no queden procesos de Chrome abiertos
        for proc in psutil.process_iter():
            if proc.name() == "chrome":
                proc.kill()

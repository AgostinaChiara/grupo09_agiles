from selenium import webdriver
import tempfile

def before_all(context):
    # Configurar el WebDriver antes de todas las pruebas
    options = webdriver.ChromeOptions()
    user_data_dir = tempfile.mkdtemp()  # Crear un directorio temporal
    options.add_argument(f'--user-data-dir={user_data_dir}')
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    # Cerrar el WebDriver después de todas las pruebas
    context.driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com"

    # Localizadores (si cambian, solo se corrigen aquí)
    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_PASSWORD = (By.ID, "password")
    BOTON_LOGIN = (By.ID, "login-button")
    MENSAJE_ERROR = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir(self):
        self.driver.get(self.URL)

    def ingresar_usuario(self, usuario):
        self.wait.until(EC.visibility_of_element_located(self.CAMPO_USUARIO)).send_keys(usuario)

    def ingresar_password(self, password):
        self.driver.find_element(*self.CAMPO_PASSWORD).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_LOGIN)).click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.MENSAJE_ERROR)).text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    BOTON_AGREGAR_MOCHILA = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOTON_QUITAR_MOCHILA = (By.ID, "remove-sauce-labs-backpack")
    BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def esta_cargada(self):
        return self.wait.until(EC.url_contains("inventory.html"))

    def agregar_mochila(self):
        self.wait.until(EC.element_to_be_clickable(self.BOTON_AGREGAR_MOCHILA)).click()
        self.wait.until(EC.visibility_of_element_located(self.BOTON_QUITAR_MOCHILA))

    def cantidad_carrito(self):
        return self.wait.until(EC.visibility_of_element_located(self.BADGE_CARRITO)).text

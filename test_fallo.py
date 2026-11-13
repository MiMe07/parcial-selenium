from login_page import LoginPage
from inventory_page import InventoryPage

def test_carrito_error_forzado(driver):
    """Falla a propósito: espera 2 productos cuando solo se agrega 1."""
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    inventario = InventoryPage(driver)
    inventario.agregar_mochila()
    assert inventario.cantidad_carrito() == "2"

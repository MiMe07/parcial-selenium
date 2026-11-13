from login_page import LoginPage
from inventory_page import InventoryPage

def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    assert InventoryPage(driver).esta_cargada()

def test_agregar_al_carrito(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    inventario = InventoryPage(driver)
    inventario.agregar_mochila()
    assert inventario.cantidad_carrito() == "1"

def test_login_fallido_usuario_bloqueado(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_usuario("locked_out_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    assert "Sorry, this user has been locked out" in login.obtener_error()

from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage

driver = webdriver.Firefox()
login = LoginPage(driver)
inventario = InventoryPage(driver)

try:
    # --- CASO 1: Login Exitoso ---
    print("Ejecutando Caso 1: Login...")
    login.abrir()
    login.ingresar_usuario("standard_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    assert inventario.esta_cargada()
    driver.save_screenshot("fase3_caso1_login.png")
    print("✅ Caso 1 completado con éxito.")

    # --- CASO 2: Agregar al Carrito ---
    print("Ejecutando Caso 2: Agregar producto...")
    inventario.agregar_mochila()
    assert inventario.cantidad_carrito() == "1"
    driver.save_screenshot("fase3_caso2_carrito.png")
    print("✅ Caso 2 completado con éxito.")

    # --- CASO 3: Login Fallido ---
    print("Ejecutando Caso 3: Login fallido...")
    driver.delete_all_cookies()
    login.abrir()
    login.ingresar_usuario("locked_out_user")
    login.ingresar_password("secret_sauce")
    login.click_login()
    assert "Sorry, this user has been locked out" in login.obtener_error()
    driver.save_screenshot("fase3_caso3_bloqueado.png")
    print("✅ Caso 3 completado con éxito.")

except Exception as e:
    print(f"❌ Error durante la ejecución: {e}")
finally:
    driver.quit()

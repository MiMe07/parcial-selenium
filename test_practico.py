from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configuración inicial
driver = webdriver.Firefox()
driver.implicitly_wait(10)

def ejecutar_pruebas():
    try:
        # --- CASO 1: Login Exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        assert "inventory.html" in driver.current_url
        driver.save_screenshot("fase1_caso1_login.png")
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al Carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge_carrito == "1"
        driver.save_screenshot("fase1_caso2_carrito.png")
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login Fallido (Usuario Bloqueado) ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()  # Limpiar sesión
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        error_msg = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
        assert "Sorry, this user has been locked out" in error_msg
        driver.save_screenshot("fase1_caso3_bloqueado.png")
        print("✅ Caso 3 completado con éxito.")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas()

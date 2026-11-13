from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)  # espera máxima de 10 s, continúa apenas se cumple la condición

def ejecutar_pruebas():
    try:
        # --- CASO 1: Login Exitoso ---
        print("Ejecutando Caso 1: Login...")
        driver.get("https://www.saucedemo.com")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        wait.until(EC.url_contains("inventory.html"))
        driver.save_screenshot("fase2_caso1_login.png")
        print("✅ Caso 1 completado con éxito.")

        # --- CASO 2: Agregar al Carrito ---
        print("Ejecutando Caso 2: Agregar producto...")
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        # Espera a que el botón cambie a "Remove" y el badge muestre 1
        wait.until(EC.visibility_of_element_located((By.ID, "remove-sauce-labs-backpack")))
        badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge.text == "1"
        driver.save_screenshot("fase2_caso2_carrito.png")
        print("✅ Caso 2 completado con éxito.")

        # --- CASO 3: Login Fallido (Usuario Bloqueado) ---
        print("Ejecutando Caso 3: Login fallido...")
        driver.delete_all_cookies()
        driver.get("https://www.saucedemo.com")
        wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
        assert "Sorry, this user has been locked out" in error.text
        driver.save_screenshot("fase2_caso3_bloqueado.png")
        print("✅ Caso 3 completado con éxito.")

    except Exception as e:
        print(f"❌ Error durante la ejecución: {e}")
        driver.save_screenshot("fase2_error.png")
    finally:
        driver.quit()

if __name__ == "__main__":
    ejecutar_pruebas()

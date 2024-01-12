import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_navigate_through_website(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")

def test_view_product_details(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    time.sleep(2)

def test_click_logo_icon(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    logo_button = driver.find_element(By.XPATH, "//a[@id='logo']")
    logo_button.click()
    time.sleep(2)

def test_add_product_to_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    time.sleep(2)

def test_delete_product_from_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(),'Delete')]")
    delete_button.click()
    time.sleep(2)

def test_view_shopping_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    time.sleep(2)

def test_proceed_to_purchase_without_products(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    shopping_cart_link = driver.find_element(By.ID, "//button[contains(text(),'Place Order')]")
    shopping_cart_link.click()
    time.sleep(2)

def test_complete_purchase_without_products(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    check_out_cart_link = driver.find_element(By.ID, "//button[contains(text(),'Place Order')]")
    check_out_cart_link.click()
    text_input1 = driver.find_element(By.XPATH, "//button[contains(text(),'Name:')]")
    text_input1.send_keys("Vlad")
    text_input2 = driver.find_element(By.XPATH, "//button[contains(text(),'Country:')]")
    text_input2.send_keys("Romania")
    text_input3 = driver.find_element(By.XPATH, "//button[contains(text(),'City:')]")
    text_input3.send_keys("Timisoara")
    text_input4 = driver.find_element(By.XPATH, "//button[contains(text(),'Credit card:')]")
    text_input4.send_keys("1234567812345678")
    text_input5 = driver.find_element(By.XPATH, "//button[contains(text(),'Month:')]")
    text_input5.send_keys("10")
    text_input6 = driver.find_element(By.XPATH, "//button[contains(text(),'Year:')]")
    text_input6.send_keys("2026")
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
    proceed_to_checkout_button.click()
    time.sleep(2)

def test_proceed_to_checkout(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
    proceed_to_checkout_button.click()
    time.sleep(2)

def test_complete_purchase(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
    proceed_to_checkout_button.click()
    text_input1 = driver.find_element(By.XPATH, "//button[contains(text(),'Name:')]")
    text_input1.send_keys("Vlad")
    text_input2 = driver.find_element(By.XPATH, "//button[contains(text(),'Country:')]")
    text_input2.send_keys("Romania")
    text_input3 = driver.find_element(By.XPATH, "//button[contains(text(),'City:')]")
    text_input3.send_keys("Timisoara")
    text_input4 = driver.find_element(By.XPATH, "//button[contains(text(),'Credit card:')]")
    text_input4.send_keys("1234567812345678")
    text_input5 = driver.find_element(By.XPATH, "//button[contains(text(),'Month:')]")
    text_input5.send_keys("10")
    text_input6 = driver.find_element(By.XPATH, "//button[contains(text(),'Year:')]")
    text_input6.send_keys("2026")
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Purchase')]")
    proceed_to_checkout_button.click()
    time.sleep(2)

def test_view_account_information(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    login_link = driver.find_element(By.ID, "login2")
    login_link.click()
    username_input = driver.find_element(By.ID, "loginusername")
    password_input = driver.find_element(By.ID, "loginpassword")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
    username_input.send_keys("puscasuvlad")
    password_input.send_keys("puscasuvlad")
    login_button.click()
    account_link = driver.find_element(By.ID, "//button[contains(text(),'Welcome puscasuvlad')]")
    account_link.click()
    time.sleep(2)

def test_logout_from_account(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    login_link = driver.find_element(By.ID, "login2")
    login_link.click()
    username_input = driver.find_element(By.ID, "loginusername")
    password_input = driver.find_element(By.ID, "loginpassword")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
    username_input.send_keys("puscasuvlad")
    password_input.send_keys("puscasuvlad")
    login_button.click()
    logout_link = driver.find_element(By.ID, "logout2")
    logout_link.click()
    time.sleep(2)

def test_navigate_to_phones_category(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    phones_category = driver.find_element(By.XPATH, "//button[contains(text(),'Phones')]")
    phones_category.click()
    driver.back()
    time.sleep(2)

def test_navigate_to_laptops_category(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    laptops_category = driver.find_element(By.XPATH, "//button[contains(text(),'Laptops')]")
    laptops_category.click()
    driver.back()
    time.sleep(2)

def test_navigate_to_monitors_category(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    monitors_category = driver.find_element(By.XPATH, "//button[contains(text(),'Monitors')]")
    monitors_category.click()
    driver.back()
    time.sleep(2)

def test_add_multiple_products_to_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_links = driver.find_elements(By.XPATH, "//div[@id='listing']//a")
    for product_link in product_links[:3]:
        product_link.click()
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
        add_to_cart_button.click()
        time.sleep(2)

def test_login_delete_product_from_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    login_link = driver.find_element(By.ID, "login2")
    login_link.click()
    username_input = driver.find_element(By.ID, "loginusername")
    password_input = driver.find_element(By.ID, "loginpassword")
    login_button = driver.find_element(By.XPATH, "//button[contains(text(),'Log in')]")
    username_input.send_keys("puscasuvlad")
    password_input.send_keys("puscasuvlad")
    login_button.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    delete_product = driver.find_element(By.ID, "Delete")
    delete_product.click()
    time.sleep(2)

def test_view_and_interact_with_featured_products(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    featured_product_links = driver.find_elements(By.XPATH, "//h4[@class='card-title']/a")
    for featured_product_link in featured_product_links:
        featured_product_link.click()
        add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
        add_to_cart_button.click()
        driver.back()
        time.sleep(2)

def test_view_about_us_page(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    privacy_policy_link = driver.find_element(By.XPATH, "//button[contains(text(),'About us')]")
    privacy_policy_link.click()
    driver.back()
    time.sleep(2)

def test_cancel_about_us_button(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    privacy_policy_link = driver.find_element(By.XPATH, "//button[contains(text(),'About us')]")
    privacy_policy_link.click()
    cancel_button = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]")
    cancel_button.click()
    time.sleep(2)
    
def test_view_contact_page(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    contact_link = driver.find_element(By.XPATH, "//button[contains(text(),'Contact')]")
    contact_link.click()
    time.sleep(2)

def test_cancel_contact_page(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    contact_link = driver.find_element(By.XPATH, "//button[contains(text(),'Contact')]")
    contact_link.click()
    cancel_link = driver.find_element(By.XPATH, "//button[contains(text(),'Close')]")
    cancel_link.click()
    time.sleep(2)

def test_send_contact_message(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    contact_link = driver.find_element(By.XPATH, "//button[contains(text(),'Contact')]")
    contact_link.click()
    text_input1 = driver.find_element(By.XPATH, "//button[contains(text(),'Contact Email:')]")
    text_input1.send_keys("vlad.puscasu02@e-uvt.ro")
    text_input2 = driver.find_element(By.XPATH, "//button[contains(text(),'Contact Name:')]")
    text_input2.send_keys("Vlad")
    text_input3 = driver.find_element(By.XPATH, "//button[contains(text(),'Message:')]")
    text_input3.send_keys("Hello there, just testing!")
    proceed_to_send_button = driver.find_element(By.XPATH, "//button[contains(text(),'Send message')]")
    proceed_to_send_button.click()
    time.sleep(2)

def test_view_and_interact_with_carousel(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    carousel = driver.find_element(By.ID, "carouselExampleSlidesOnly")
    next_button = driver.find_element(By.XPATH, "//button[@class='carousel-next-button']")
    back_button = driver.find_element(By.XPATH, "//button[@class='carousel-back-button']")
    next_button.click()
    next_button.click()
    next_button.click()
    back_button.click()
    back_button.click()
    back_button.click()
    time.sleep(2)

def test_add_phone_laptop_monitor_to_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    phones_category = driver.find_element(By.XPATH, "//button[contains(text(),'Phones')]")
    phones_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button.click()
    laptops_category = driver.find_element(By.XPATH, "//button[contains(text(),'Laptops')]")
    laptops_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    monitors_category = driver.find_element(By.XPATH, "//button[contains(text(),'Monitors')]")
    monitors_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    time.sleep(2)

def test_add_and_delete_phone_laptop_monitor_from_cart(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    phones_category = driver.find_element(By.XPATH, "//button[contains(text(),'Phones')]")
    phones_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button.click()
    laptops_category = driver.find_element(By.XPATH, "//button[contains(text(),'Laptops')]")
    laptops_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    monitors_category = driver.find_element(By.XPATH, "//button[contains(text(),'Monitors')]")
    monitors_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(),'Delete')]")
    product_links = driver.find_elements(By.XPATH, "//h4[@class='card-title']/a")
    for product_link in product_links:
        delete_button.click()
    time.sleep(2)

def test_view_and_refresh_about_us_page(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    privacy_policy_link = driver.find_element(By.XPATH, "//button[contains(text(),'About us')]")
    privacy_policy_link.click()
    play_button = driver.find_element(By.CLASS_NAME, "ytp-play-button")
    play_button.click()
    time.sleep(3)
    driver.refresh()
    time.sleep(2)

def test_view_contact_page_and_fill_and_refresh(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    contact_link = driver.find_element(By.XPATH, "//button[contains(text(),'Contact')]")
    contact_link.click()
    text_input1 = driver.find_element(By.XPATH, "//button[contains(text(),'Contact Email:')]")
    text_input1.send_keys("vlad.puscasu02@e-uvt.ro")
    text_input2 = driver.find_element(By.XPATH, "//button[contains(text(),'Contact Name:')]")
    text_input2.send_keys("Vlad")
    text_input3 = driver.find_element(By.XPATH, "//button[contains(text(),'Message:')]")
    text_input3.send_keys("Hello there, just testing!")
    driver.refresh()
    contact_link.click()
    time.sleep(2)

def test_proceed_to_checkout_and_refresh(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    proceed_to_checkout_button = driver.find_element(By.XPATH, "//button[contains(text(),'Place Order')]")
    proceed_to_checkout_button.click()
    driver.refresh()
    time.sleep(2)

def test_objects_to_cart_and_refresh_and_delete(setup_browser):
    driver = setup_browser
    driver.get("https://www.demoblaze.com/")
    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    phones_category = driver.find_element(By.XPATH, "//button[contains(text(),'Phones')]")
    phones_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    driver.refresh()
    driver.back()
    laptops_category = driver.find_element(By.XPATH, "//button[contains(text(),'Laptops')]")
    laptops_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    driver.refresh()
    driver.back()
    monitors_category = driver.find_element(By.XPATH, "//button[contains(text(),'Monitors')]")
    monitors_category.click()
    product_link = driver.find_element(By.XPATH, "//div[@id='listing']//a")
    product_link.click()
    add_to_cart_button.click()
    shopping_cart_link = driver.find_element(By.ID, "cartur")
    shopping_cart_link.click()
    driver.refresh()
    driver.back()
    shopping_cart_link.click()
    delete_button = driver.find_element(By.XPATH, "//button[contains(text(),'Delete')]")
    product_links = driver.find_elements(By.XPATH, "//h4[@class='card-title']/a")
    for product_link in product_links:
        delete_button.click()
    time.sleep(2)
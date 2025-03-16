from selenium.webdriver.common.by import By

class Locators:
    CATEGORY_KADIN = (By.LINK_TEXT, 'KADIN')
    CATEGORY_YELEK = (By.LINK_TEXT, 'Yelek')
    FIRST_PRODUCT = (By.CSS_SELECTOR, '.product-card:nth-of-type(1)')
    SIZE_OPTION_M = (By.XPATH, "//button[contains(text(),'M')]")
    ADD_TO_CART = (By.XPATH, "//button[contains(@class, 'add-to-card')]")
    GO_TO_CART_BUTTON = (By.XPATH, "//a[contains(@href, '/sepetim')]")
    COOKIE_REJECT_BUTTON = (By.XPATH, "//button[contains(text(),'Tüm Çerezleri Reddet')]")
    CART_COUNT = (By.XPATH, "//span[@class='badge-circle']")

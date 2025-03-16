from locators import Locators
from base_page import BasePage
from selenium.webdriver import ActionChains

class AddToCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def disable_cookies(self):
        try:
            self.click(Locators.COOKIE_REJECT_BUTTON)
            print("**Tüm çerezler reddedildi.**")
        except Exception as e:
            print(f"**Çerez popup'ı görünmüyor veya reddetme hatası: {e}**")

    def select_category(self):
        kategori_kadin = self.is_element_visible(Locators.CATEGORY_KADIN)
        ActionChains(self.driver).move_to_element(kategori_kadin).perform()
        self.click(Locators.CATEGORY_YELEK)

    def select_first_product(self):
        self.scroll_to_element(Locators.FIRST_PRODUCT)
        self.click(Locators.FIRST_PRODUCT)

    def select_size_m(self):
        try:
            self.execute_script_click(Locators.SIZE_OPTION_M)
            print("**M bedeni seçildi.**")
        except Exception as e:
            print(f"** M bedeni seçimi hatası: {e}**")

    def add_to_cart(self):
        try:
            self.scroll_to_element(Locators.ADD_TO_CART)
            self.execute_script_click(Locators.ADD_TO_CART)
            print("**Ürün sepete eklendi.**")
        except Exception as e:
            print(f"**Sepete ekleme hatası: {e}**")

    def go_to_cart(self):
        try:
            self.click(Locators.GO_TO_CART_BUTTON)
            print("**Sepetime git tıklandı.**")
        except Exception as e:
            print(f"**'Sepetime Git' tıklama hatası: {e}**")

    def verify_cart(self):
        try:
            cart_count = self.get_text(Locators.CART_COUNT)
            assert cart_count == '1', '** Sepette eksik veya hiç ürün eklenmedi.**'
            print("**Ürün sepette doğrulandı.**")
        except Exception as e:
            print(f"**Sepet kontrol hatası: {e}**")

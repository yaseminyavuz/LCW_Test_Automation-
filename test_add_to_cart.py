import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from add_to_cart_page import AddToCartPage

class TestAddToCart(unittest.TestCase):
    base_url = 'https://www.lcw.com/'

    def setUp(self):
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-plugins")
        options.add_argument("--disable-cookies")
        options.add_argument("--incognito")
        options.add_argument("--disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.page = AddToCartPage(self.driver)

        # Çerezleri reddet
        self.page.disable_cookies()

    def test_add_product_to_cart(self):
        print("\n** Test: Ürün Sepete Ekleme Başlatıldı **\n")

        # Kategori seç
        self.page.select_category()

        # Ürün seç
        self.page.select_first_product()

        # Beden seç
        self.page.select_size_m()

        # Sepete ekle
        self.page.add_to_cart()

        # Sepetime git
        self.page.go_to_cart()

        # Sepeti kontrol et
        self.page.verify_cart()

        print("\n*** Test Başarıyla Tamamlandı ***\n")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

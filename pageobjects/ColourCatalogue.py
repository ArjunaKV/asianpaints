from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

element_to_hover_over = None


class ColourCatalogue:
    def __init__(self, driver):
        self.driver = driver

    def get_view_cart(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button")

    def click_view_cart(self):
        self.get_view_cart().click()

    def get_search_bar(self):
        return self.driver.find_element(By.NAME, "q")

    def enter_search_name(self, text):
        self.get_search_bar().send_keys(text)

    def get_search_button(self):
        return self.driver.find_element(By.CLASS_NAME, "js-header-search-handle")

    def click_search_button(self):
        self.get_search_button().click()

    def get_paint_name1(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div[1]/div[2]/div/div/section/div/div/div[2]/div/div["
                                        "1]/div/div["
                                        "2]/div/a[1]/div")

    def click_paint1(self):
        self.get_paint_name1().click()

    def get_check_pincode_bar1(self):
        return self.driver.find_element(By.ID, "checkPincode")

    def enter_pincode_number1(self, pincodenumber1):
        self.get_check_pincode_bar1().send_keys(pincodenumber1)

    def get_check_button1(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div[2]/div/div[2]/div/div[7]/div/form/div[1]/div["
                                        "1]/button")

    def click_check_button1(self):
        self.get_check_button1().click()

    def get_add_to_cart_button1(self):
        return self.driver.find_element(By.ID, "add-to-cart-click")

    def click_add_to_cart_button1(self):
        self.get_add_to_cart_button1().click()

    def get_paint_name_options(self):
        return self.driver.find_element(By.LINK_TEXT, "Exterior Textures")

    def click_paint_name_options(self):
        self.get_paint_name_options().click()

    def get_paint_name2(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"plpListing\"]/section[2]/div[2]/ul/li[2]/a/span")

    def click_paint_name2(self):
        self.get_paint_name2().click()

    def get_check_pincode_bar2(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"checkPincode\"]")

    def enter_pincode_number2(self, pincodenumber2):
        self.get_check_pincode_bar2().send_keys(pincodenumber2)

    def get_check_button2(self):
        return self.driver.find_element(By.XPATH,
                                        "/html/body/div[1]/div/div[2]/div/div[2]/div/div[8]/div/form/div[1]/div["
                                        "1]/button")

    def click_check_button2(self):
        self.get_check_button2().click()

    def get_add_to_cart_button2(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"add-to-cart-click\"]")

    def click_add_to_cart_button2(self):
        self.get_add_to_cart_button2()

    def get_remove_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/span")

    def click_remove_button(self):
        self.get_remove_button().click()

    def get_redirect_page(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/a/img")

    def click_redirect_page(self):
        self.get_redirect_page().click()

    def total_name_display(self):
        a = self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/h2/span")
        print(a.is_displayed())

    def total_amount_dispay(self):
        element = self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/h2/label")
        print(element.is_displayed())

    def get_checkout_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/div/div/div[2]/div/div/a")

    def click_checkout_button(self):
        self.get_checkout_button().click()

    def get_login_mobile_bar(self):
        return self.driver.find_element(By.ID, "loginMobile")

    def enter_login_mobile_number(self, mobilenumber):
        self.get_login_mobile_bar().send_keys(mobilenumber)

    def click_submit(self):
        self.get_login_mobile_bar().submit()

    def get_increase_product1(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id=\"header-minicart\"]/div/div/div/ul/li[1]/div/div/div/div/span["
                                        "2]/button")

    def click_increase_product1(self):
        self.get_increase_product1().click()

    def get_increase_product2(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@id=\"header-minicart\"]/div/div/div/ul/li[2]/div/div/div/div/span["
                                        "2]/button")

    def click_increase_product2(self):
        self.get_increase_product2().click()

    def get_decrease_product1(self):
        return self.driver.find_element(By.ID, "cart-quantity-minus0")

    def click_decrease_product1(self):
        self.get_decrease_product1().click()

    def get_decrease_product2(self):
        return self.driver.find_element(By.ID, "cart-quantity-minus1")

    def click_decrease_product2(self):
        return self.get_decrease_product2().click()

    def hover_paint_name(self):
        a = self.driver.find_element(By.XPATH,
                                     "//*[@id=\"headerNav\"]/div[1]/ul/li[1]/a[2]/span[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(a).perform()


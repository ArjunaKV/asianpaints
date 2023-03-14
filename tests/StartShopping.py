from selenium.webdriver.common.by import By


class StartShopping:
    def __init__(self, driver):
        self.driver = driver

    def get_view_cart(self):
        return self.driver.find_element(By.XPATH, "//*[@id=\"header-minicart\"]/div/button")

    def click_view_cart(self):
        self.get_view_cart().click()

    def get_start_shopping(self):
        return self.driver.find_element(By.CLASS_NAME,"ctaText")

    def click_start_shopping(self):
        self.get_start_shopping().click()



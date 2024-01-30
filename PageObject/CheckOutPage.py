from selenium.webdriver.common.by import By

from PageObject.LastBlock import LastBlock


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
        self.card = (By.XPATH, '//div[@class="card h-100"]')
        self.Primary = (By.CSS_SELECTOR, 'a[class="nav-link btn btn-primary"]')
        self.Submit = (By.CSS_SELECTOR, 'button[class="btn btn-success"]')

    def CardItems(self):
        return self.driver.find_elements(*self.card)

    def Button(self):
        return self.driver.find_element(*self.Primary)

    def btn_Suck(self):
        return self.driver.find_element(*self.Submit)





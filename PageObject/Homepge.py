from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from PageObject.CheckOutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.shop = (By.CSS_SELECTOR, "a[href*='shop']")
        self.name = (By.NAME, "name")
        self.email = (By.NAME, "email")
        self.password = (By.CSS_SELECTOR, "#exampleInputPassword1")
        self.checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
        self.dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
        self.checkbox1 = (By.CSS_SELECTOR, 'input[value="option1"]')
        self.Dob = (By.NAME, "bday")
        self.submit = (By.CSS_SELECTOR, 'input[type="submit"]')
        self.verify = (By.XPATH, "/html/body/app-root/form-comp/div/div[2]/div")

    def ShopItem(self):
        self.driver.find_element(*self.shop).click()
        checkoutPage = CheckOutPage(self.driver)   # checkoutpage = CheckOutPage(self.driver)
        return checkoutPage

    def WriteName(self):
        return self.driver.find_element(*self.name)

    def WriteEmail(self):
        return self.driver.find_element(*self.email)

    def WritePassword(self):
        return self.driver.find_element(*self.password)

    def WriteCheckbox(self):
        return self.driver.find_element(*self.checkbox)

    def WriteDropdown(self):
        return self.driver.find_element(*self.dropdown)

    def WriteCheckbox1(self):
        return self.driver.find_element(*self.checkbox1)

    def WriteDob(self):
        return self.driver.find_element(*self.Dob)

    def WriteSubmit(self):
        return self.driver.find_element(*self.submit)

    def WriteVerify(self):
        return self.driver.find_element(*self.verify)

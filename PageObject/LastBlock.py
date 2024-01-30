from selenium.webdriver.common.by import By


class LastBlock:

    def __init__(self, driver):
        self.driver = driver
        self.country = (By.CSS_SELECTOR, "#country")
        self.submit = (By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']")
        self.success = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
        self.Alert = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")

    def select_process(self):
        return self.driver.find_element(*self.country)

    def Checkbox(self):
        return self.driver.find_element(*self.submit)

    def ButtonSuccess(self):
        return self.driver.find_element(*self.success)

    def Validation(self):
        return self.driver.find_element(*self.Alert)

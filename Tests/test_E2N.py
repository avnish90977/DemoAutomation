from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PageObject.CheckOutPage import CheckOutPage
from PageObject.Homepge import HomePage
from PageObject.LastBlock import LastBlock
from usages.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_E2N(self):
        log = self.getlLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.ShopItem()
        phones = checkoutpage.CardItems()
        for phone in phones:
            names = phone.find_element(By.XPATH, "div/h4/a")
            log.info("names of phone displayed as " + "names")  # Log code
            if names == "Blackberry":
                phone.find_element(By.XPATH, "div/button").click()
        checkoutpage.Button().click()
        checkoutpage.btn_Suck().click()
        lastblock = LastBlock(self.driver)
        log.info("Expecting Country Name here")
        lastblock.select_process().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India"))).click()
        #self.VerifyLinkPresent("India").click()
        lastblock.Checkbox().click()
        lastblock.ButtonSuccess().click()
        text = lastblock.Validation().text
        log.info("message for validation after the test" + "text")
        assert "Your order will be delivered " in text
        print("Everything Executed")











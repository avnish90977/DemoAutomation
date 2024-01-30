import pytest

from PageObject.Homepge import HomePage
from TestData.HomePageData import HomePageData
from usages.BaseClass import BaseClass


class TestDemo1(BaseClass):

    def test_formSubmission(self, getdata): #getdata
        log = self.getlLogger()
        homepage = HomePage(self.driver)
        log.info("first name = " + getdata["FirstName"])
        homepage.WriteName().send_keys(getdata["FirstName"])
        homepage.WriteEmail().send_keys(getdata["Email"])
        homepage.WritePassword().send_keys(getdata["Password"])
        homepage.WriteCheckbox().click()
        self.SelectOptionsByIndex(homepage.WriteDropdown(), getdata["Gender"])
        homepage.WriteCheckbox1()
        homepage.WriteDob().send_keys(16122000)
        homepage.WriteSubmit().click()
        validation = homepage.WriteVerify().text
        log.info("popup message from test is0" + validation)
        assert "The Form has been submitted successfully!." in validation
        print("Everything Looks Fine in HOME_Page ")
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getdata(self, request):
        return request.param

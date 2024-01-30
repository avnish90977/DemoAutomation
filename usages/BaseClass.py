import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def SelectOptionsByIndex(self, locator, index):
        Dropdown = Select(locator)
        Dropdown.select_by_index(0)
        # used for below case
        '''Dropdown = Select(homepage.WriteDropdown())
        Dropdown.select_by_index(0)'''

    # def VerifyLinkPresent(self, text):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getlLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger





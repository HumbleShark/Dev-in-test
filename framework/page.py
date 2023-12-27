class Page:

    def __init__(self, driver):
        self.driver = driver
        if self.driver.is_locked():
            raise ProtectedDeviceException
    def find_element(self, by, value, multiple=False):
        # Would be so much better with AppiumBy from newer versions...
        if not multiple:
            if by == "class":
                return self.driver.find_element_by_class_name(value)
            elif by == "id":
                return self.driver.find_element_by_id(value)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(value)
            elif by == "name":
                # locale sensitive!
                return self.driver.find_element_name(value)
        else:
            if by == "class":
                return self.driver.find_elements_by_class_name(value)
            elif by == "id":
                return self.driver.find_elements_by_id(value)
            elif by == "xpath":
                return self.driver.find_elements_by_xpath(value)
            elif by == "name":
                # locale sensitive!
                return self.driver.find_elements_by_name(value)


    def click_element(self, element):
        element.click()


class ProtectedDeviceException(Exception):
    "Raised when the device is password protected"
    pass


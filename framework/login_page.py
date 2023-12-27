from .page import Page

class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.find_element(by="class", value="android.widget.TextView", multiple=True)[1].click()  # log in button

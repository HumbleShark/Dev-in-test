import time

import pytest
from selenium.common.exceptions import NoSuchElementException

import logging
LOGGER = logging.getLogger()


class SynchronizationTimeout(Exception):
    "Raised after 3 'Synchronizing with the server, please wait' messages"
    print("Can't synchronize with server!")


@pytest.mark.parametrize("username,password,success",
                         [("1", "1", False),
                          ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
                          ("abc@notmail.com", "1", False)])
def test_user_login(user_login_fixture, username, password, success):
    LOGGER.info(f"Starting test: {username} - {password}")
    while True:
        fields = user_login_fixture.find_element(by="class", value="android.widget.EditText", multiple=True)
        if len(fields) > 0:
            break
        # if logged in, sign out
        else:
            LOGGER.info(f"Already logged in, signing out")
            try:
                user_login_fixture.find_element(by="id", value="com.ajaxsystems:id/backButton").click()
            except NoSuchElementException:
                pass
            user_login_fixture.find_element(by="id", value="com.ajaxsystems:id/menuDrawer").click()
            user_login_fixture.find_element(by="xpath", value='(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage"])[1]').click()
            user_login_fixture.find_element(by="xpath",
                                            value='(//android.view.View[@resource-id="com.ajaxsystems:id/atomImage"])[5]').click()
            user_login_fixture.find_element(by="class", value="android.widget.TextView", multiple=True)[1].click()
    while True:
        fields[0].clear().send_keys(username)  # login field
        fields[1].clear().send_keys(password)  # password field

        # log in button
        user_login_fixture.find_element(by="class", value="android.widget.TextView", multiple=True)[5].click()
        attempts = 0
        LOGGER.info(f"Attempting login")
        try:
            error = user_login_fixture.find_element(by="xpath", value='//*[@resource-id="com.ajaxsystems:id/snackbar_text"]')
            LOGGER.info(f"Got error box: {error.get_attribute('text')}")
            if error.get_attribute('text') == "Synchronizing with the server, please wait":
                attempts += 1
                if attempts >= 3:
                    LOGGER.error(f"Maximum attempts reached, throwing an exception!")
                    raise SynchronizationTimeout
                LOGGER.info(f"Waiting before retry...")
                time.sleep(15)
                continue
            successful = False
            break
        except NoSuchElementException:
            successful = True
            break
    LOGGER.info(f"Login attempt result successful: {successful}")
    if (successful == success):
        LOGGER.info("As expected. Test passed!")
    else:
        LOGGER.warning("Not expected! Test failed!")
    assert successful == success


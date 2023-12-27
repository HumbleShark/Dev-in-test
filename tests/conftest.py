import subprocess
import time
import logging

import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities

LOGGER = logging.getLogger()

@pytest.fixture(scope='session')
def run_appium_server():
    LOGGER.info("Setting up Appium server")
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)

@pytest.fixture(scope='session')
def driver(run_appium_server):
    LOGGER.info("Setting up driver")
    driver = webdriver.Remote('http://localhost:4723', android_get_desired_capabilities())
    driver.implicitly_wait(5)
    yield driver
    LOGGER.info("Testing done, stopping driver")
    LOGGER.info("-"*50)
    driver.quit()

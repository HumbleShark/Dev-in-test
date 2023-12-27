import subprocess
import logging

LOGGER = logging.getLogger()

def android_get_desired_capabilities():
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True, check=True)
    output_lines = result.stdout.strip().split('\n')
    devices = [line.split('\t')[0] for line in output_lines[1:] if line.strip()]
    LOGGER.info(f"Found device: {devices[0]}")
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': devices[0],
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'language': 'en',
        'locale': 'US'
    }


from appium import webdriver


def get_driver():
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": "com.android.mms",
        "appActivity": ".ui.ConversationList",
        "resetKeyboard": True,
        "unicodeKeyboard": True
    }
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)

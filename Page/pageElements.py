from selenium.webdriver.common.by import By


class PageElements:
    # 定位新建
    search_01 = (By.ID, "com.android.mms:id/action_compose_new")
    # 定位收件人
    search_02 = (By.ID, "com.android.mms:id/recipients_editor")
    # 定位输入框
    search_03 = (By.ID, "com.android.mms:id/embedded_text_editor")
    # 定位发送键
    search_04 = (By.ID, "com.android.mms:id/send_button_sms")
    # 定位发送内容
    search_05 = (By.ID, "com.android.mms:id/text_view")

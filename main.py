import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

qrSucces = False
LOGIN = "_3GlyB"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
#time.sleep(30)


def verificarOnline(LOGIN):
    try:
        login = driver.find_element(By.CLASS_NAME, LOGIN)
        return login.is_displayed()
    except:
        return False


if not verificarOnline(LOGIN):
    while not qrSucces:
        if verificarOnline(LOGIN):
            qrSucces = True
        else:
            print("")
        print("Contando")
        time.sleep(2)
    print("Logou!")



# qrCode = driver.find_element(By.XPATH, "//canvas[@role='img']").is_displayed()

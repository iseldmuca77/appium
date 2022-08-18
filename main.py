import code
import email
from shutil import ExecError
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from random import randint


desired_cap ={
    "deviceName": "be39be96",
    "platformName": "Android"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(30)

#driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button[1]').click()
#key code per enter
#driver.press_keycode(66)


"""
#driver.press_keycode(279)
###        Hap turbo VPN     ###
turbo_vpn = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Turbo VPN"]')
turbo_vpn.click()
time.sleep(randint(4,5))

#Futemi ne proxy
try:
    tap_to_connect_btn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]')
    tap_to_connect_btn.click()
    time.sleep(30)
except Exception as e:
    time.sleep(randint(35,40))
    driver.press_keycode(4)
    tap_to_connect_btn1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView[2]')
    tap_to_connect_btn1.click()
    time.sleep(30)

#Dalim nga turbo vpn
driver.press_keycode(187)
time.sleep(randint(3,4))
driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Close"]').click()
time.sleep(randint(2,3))
"""


###        Hap tempmail      ###
try:
    temp_button = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Temp Mail"]')
    temp_button.click()
    time.sleep(randint(3,5))
except Exception as e:
    try:
        driver.press_keycode(4)
        time.sleep(2)
        temp_button = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Temp Mail"]')
        temp_button.click()
        time.sleep(randint(3,5))
    except Exception as e:
        driver.press_keycode(4)
        time.sleep(randint(3,5))
        temp_button = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Temp Mail"]')
        temp_button.click()


time.sleep(randint(1,3))
###        free trial button  ###
#kryq_button2 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.Button')
#kryq_button2.click()

time.sleep(randint(4,5))

###        Copy button       ###
try:
    copy_button = driver.find_element_by_id('com.tempmail:id/btnCopy')
    copy_button.click()
    time.sleep(randint(3,4))
except Exception as e:
    #Try premium
    time.sleep(randint(3,4))
    x_button = driver.find_element_by_id('	com.tempmail:id/ivClose')
    x_button.click()
    print(e)
    time.sleep(randint(2,3))
    copy_button = driver.find_element_by_id('com.tempmail:id/btnCopy')
    copy_button.click()
    time.sleep(randint(3,4))


###        back button      187###
driver.press_keycode(4)
time.sleep(randint(3,4))

###        Hap google        ###
#Nese klikon copy button dhe pastaj i del nje reklam i duhet te pres prap per reklamen
chrome_start = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Firefox"]')
chrome_start.click()

time.sleep(randint(8,10))

###       Email section   ###
#klikon ne seksionin e email
email_section = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.CheckBox[2]")
email_section.click() 
time.sleep(randint(5,7))

###       Paste email ne email_field            ###
email_field = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
email_field.click()
time.sleep(randint(1,2))
email_field1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText')
email_field1.click()
time.sleep(randint(4,5))
#paste keycode
driver.press_keycode(279)
time.sleep(randint(3,4))


###       Next Button      ###
next_btn = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[3]')
next_btn.click()
time.sleep(randint(3,4))

def confirmation_code():
    #Shkojme ne dritaren temp_mail
    temp_mail_window = 	driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Temp Mail"]')
    temp_mail_window.click()
    time.sleep(randint(2,3))
    #shkojme ne seksionin inbox
    inbox_section = driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Inbox"]/android.widget.FrameLayout')
    inbox_section.click()
    time.sleep(randint(4,5))
    #kliojme per kodin
    #nese nuk gjendet presim
    try:
        code_section = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
        code_section.click()
    except Exception as e:
        time.sleep(randint(30,60))
        code_section1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup')
        code_section1.click()

    time.sleep(randint(3,4))
    #kopjome tekstin e kodit
    kodi = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[7]').text
    #marrim vetme 6 karakteret e para
    code = kodi[:6]
    return code

def enter_confirmation_code():
    #shkojme ne dritaren firefox
    instagram_firefox_window = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Firefox"]')
    instagram_firefox_window.click()
    time.sleep(randint(3,4))
    #shkruajme kodin 
    confirmation_code_field = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.EditText')
    confirmation_code_field.send_keys(code)
    time.sleep(randint(3,4))
    #klikojme next
    next_button1 = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.Button')
    next_button1.click()

driver.press_keycode(187)
time.sleep(randint(2,3))

confirmation_code()

driver.press_keycode(187)
time.sleep(randint(2,3))

enter_confirmation_code()
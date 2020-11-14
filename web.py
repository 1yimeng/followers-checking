from selenium import webdriver
import time
import math
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
PATH ="/Users/yimengwang/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)



driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys("peachy.1m")

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys("wang236611161")

button = driver.find_element_by_css_selector("button[type=submit]")
button.click()

time.sleep(4)

icon = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
icon.click()

time.sleep(2)

profile = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
profile.click()

time.sleep(3)
followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
followers.click()
time.sleep(3)

all_followers = int(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li['
                                                       '2]/a/span').get_attribute("title").replace(".",""))
scroll_times = int(math.floor(all_followers/12)+1) #rounds down and ad one for the rest
for i in range(scroll_times):
    follower_names = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']") #hardcoded tag, fix for later use
    real_names = [x.text for x in follower_names]
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight
    ''')
    time.sleep(2)

print(real_names)
print(len(real_names))
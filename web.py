from selenium import webdriver
import time
import math

user_name = input("Enter username:")
user_pass = input("Enter password:")

PATH ="/Users/yimengwang/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
username = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
username.send_keys(user_name)

password = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
password.send_keys(user_pass)

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

all_followers = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li['
                                                       '2]/a/span').get_attribute("title").replace(".","")
try:
    all_followers = int(all_followers)
except ValueError:
    all_followers = list(all_followers)
    del all_followers[1]
    "".join(all_followers)
    all_following = int(all_followers)

scroll_times = int(math.floor(all_followers/12)+1)  # rounds down and ad one for the rest
for i in range(scroll_times):
    follower_names = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
    real_names = [x.text for x in follower_names]
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight
    ''')
    time.sleep(2)

xclose = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
xclose.click()
time.sleep(3)

following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
following.click()
time.sleep(3)

all_following = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text

try:
    all_following = int(all_following)
except ValueError:
    all_following = list(all_following)
    del all_following[1]
    "".join(all_following)
    all_following = int(all_following)

scroll_times2 = int(math.floor(all_following/12)+1)  # rounds down and ad one for the rest
for i in range(scroll_times2):
    following_names = driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")  # hardcoded tag, fix for later use
    following_total = [x.text for x in following_names]
    driver.execute_script('''
        var fDialog = document.querySelector('div[role="dialog"] .isgrP');
        fDialog.scrollTop = fDialog.scrollHeight
    ''')
    time.sleep(2)

not_following_back = []
for i in range(all_following):
    if following_total[i] not in real_names:
        not_following_back.append(following_total[i])

print(not_following_back)
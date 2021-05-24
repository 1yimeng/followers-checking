from selenium import webdriver
import time
import math

# always sleeps at the end to keep it consistent
PATH = "/Users/yimengwang/Downloads/chromedriver"

class Webpage:
    def __init__(self, PATH, user_name, user_pass):
        self.path = PATH
        self.driver = webdriver.Chrome(PATH)
        self.user_name =  user_name
        self.user_pass = user_pass

    def opening_ig(self):
        '''
        Opens Instagram with driver

        Argument: none
        Return: none
        '''
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4)

    def login(self):
        username = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input")
        username.send_keys(self.user_name)

        password = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input")
        password.send_keys(self.user_pass)

        button = self.driver.find_element_by_css_selector("button[type=submit]")
        button.click()

        time.sleep(6)

    def click_profile_icon(self):
        icon = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        icon.click()
        time.sleep(2)

    def to_own_profile(self):
        '''
        Must be used after click_profile_icon
        '''
        profile = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
        profile.click()
        time.sleep(3)

    def open_followers(self):
        followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        time.sleep(3)

    def get_num_followers(self):
        all_followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li['
                                                       '2]/a/span').get_attribute("title").replace(".","")
        try:
            all_followers = int(all_followers)
        except ValueError:
            all_followers = list(all_followers)
            del all_followers[1]
            again = "".join(all_followers)
            all_followers = int(again)

        print("You have %d followers." % all_followers)
        return all_followers

    def get_followers(self, all_followers):
        scroll_times = int(math.floor(all_followers/12)+1)  # rounds down and ad one for the rest
        for i in range(scroll_times):
            follower_names = self.driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
            real_names = [x.text for x in follower_names]
            self.driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
            time.sleep(2)

        print(f'The collected number of followers is {len(real_names)}.')

        xclose = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")
        xclose.click()
        time.sleep(3)
        return real_names

    def get_num_following(self):
        following = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
        following.click()
        time.sleep(3)

        all_following = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span').text

        try:
            all_following = int(all_following)
        except ValueError:
            all_following = list(all_following)
            del all_following[1]
            new = "".join(all_following)
            all_following = int(new)

        print("You are following %d people." % all_following)
        return all_following
    
    def get_following(self, all_following):
        scroll_times2 = int(math.floor(all_following/12)+1)  # rounds down and ad one for the rest
        # print(scroll_times2)
        for i in range(scroll_times2):
            following_names = self.driver.find_elements_by_xpath("//span[@class='Jv7Aj mArmR MqpiF  ']")
            following_total = [x.text for x in following_names]
            self.driver.execute_script('''
                var fDialog = document.querySelector('div[role="dialog"] .isgrP');
                fDialog.scrollTop = fDialog.scrollHeight
            ''')
            time.sleep(2)

        print(f'The collected number of following users is {len(following_total)}.')
        return following_total

    def not_following_you_back(self, following, followers):
        not_following_back = []
        for i in range(len(following)):
            if following[i] not in followers:
                not_following_back.append(following[i])

        print('The users that are not following you back are: ')
        for i in range(len(not_following_back)-1):
            print(not_following_back[i], end=', ')
        print(not_following_back[len(not_following_back)-1])

if __name__ == "__main__":
    user_name = input("Enter username: ")
    user_pass = input("Enter password: ")
    driver = Webpage(PATH, user_name, user_pass)
    driver.opening_ig()
    driver.login()
    driver.click_profile_icon()
    driver.to_own_profile()
    driver.open_followers()
    followers_num = driver.get_num_followers()
    all_followers = driver.get_followers(followers_num)
    following_num = driver.get_num_following()
    all_following = driver.get_following(following_num)
    driver.not_following_you_back(all_following, all_followers)
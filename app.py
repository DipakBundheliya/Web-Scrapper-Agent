from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def web_login(web_link="https://x.com/login"):
    driver = webdriver.Chrome()
    driver.get(web_link)
    time.sleep(5) # Wait to load page , x , y
    print("checking...")
    username_field = driver.find_element(By.XPATH , '//input[@name="text" and @type="text" and contains(@class , "r-30o5oe")]')
    username_field.send_keys("x")
    time.sleep(3)
    next_button = username_field.find_element(By.XPATH , '//span[text() = "Next"]')
    next_button.click()
    time.sleep(3)
    username_field = driver.find_element(By.XPATH , '//input[@name="password" and @type="password" and contains(@class , "r-30o5oe")]')
    username_field.send_keys("y")
    time.sleep(3)
    login_button = username_field.find_element(By.XPATH , '//span[text() = "Log in"]')
    login_button.click()
    time.sleep(15)
    tweet_descriptions = []


    def scroll_page():
        for _ in range(3):
            driver.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
            time.sleep(3)
    
    for _ in range(5):
        tweets = driver.find_elements(By.XPATH , '//div[@data-testid = "tweetText"]' )
        tweet_descriptions = tweet_descriptions + [tweet.text for tweet in tweets]  
        print("tweets length are ", len(tweet_descriptions))
        scroll_page()

    tweets = driver.find_elements(By.XPATH , '//div[@data-testid = "tweetText"]' )
    print("Total tweets length are ", len(tweets))
    for i , description in enumerate(tweet_descriptions , start=1):
        print(f"Tweet {i} , {description}")

web_login()
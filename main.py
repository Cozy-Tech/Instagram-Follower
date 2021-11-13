from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import re


class CozyInsta:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Edge(r"H:\Jupyter\msedgedriver.exe")
        
    def login(self):
        browser = self.browser
        browser.get("https://www.instagram.com/")
        
        accept = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Accept All")]')))
        accept.click()
        
        username = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="username"]')))
        username.send_keys(self.username)
        
        password = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="password"]')))
        password.send_keys(self.password)
        
        time.sleep(2)
        
        login = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]')))
        login.click()
        
        
    def search(self,keyword):
        browser = self.browser
        browser.get(f"https://www.instagram.com/explore/tags/{keyword}/")
        time.sleep(5)
        
        for _ in range(2):
            browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            
        links = browser.find_elements_by_tag_name("a")
        links2 = [posts.get_attribute("href") for posts in links]
        
        r = re.compile("https://www.instagram.com/p/(\S)*")
        
        self.links_fixed = []
        
        for link in links:
            self.links_fixed = list(filter(r.match,links2))
        
        print(f"{len(self.links_fixed)} posts found.")
        
        
    def like(self):
        browser = self.browser
        likes = 1
        
        for link in self.links_fixed:
            browser.get(link)
            like = WebDriverWait(browser,30).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="QBdPU rrUvL"]//*[name()="svg"][@aria-label="Like"]')))
            like.click()
            print(f"{likes} Liked!")
            likes += 1
            time.sleep(3)
        
    
cozytech = CozyInsta("cozytechchannel","TKaEPvH\w-$+6k;)")
cozytech.login()
time.sleep(5)
cozytech.search("کفش")
cozytech.like()

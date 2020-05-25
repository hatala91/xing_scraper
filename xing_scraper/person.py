import requests
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .functions import time_divide
from .objects import Interest, Accomplishment, Organisation, Qualification, Scraper
import os

class Person(Scraper):
    name = None
    interests = []
    accomplishments = []
    organisations = []
    qualifications = []
    xing_url = None

    def __init__(self, xing_url = None, driver = None, get = True, scrape = True, close_on_complete = True):
        self.xing_url = xing_url

        if driver is None:
            try:
                if os.getenv("CHROMEDRIVER") == None:
                    driver_path = os.path.join(os.path.dirname(__file__), 'drivers/chromedriver')
                else:
                    driver_path = os.getenv("CHROMEDRIVER")

                driver = webdriver.Chrome(driver_path)
            except:
                driver = webdriver.Chrome()

        if get:
            driver.get(xing_url)

        self.driver = driver

        if scrape:
            self.scrape(close_on_complete)

    def add_interest(self, interest):
        self.interests.append(interest)
        
    def add_accomplishment(self, accomplishment):
        self.accomplishments.append(accomplishment)
		
    def add_organisation(self, organisation):
        self.organisations.append(organisation)
        
    def add_qualification(self, qualification):
        self.qualifications.append(qualification)

    def scrape(self, close_on_complete = True):
        self.scrape_logged_in(close_on_complete = close_on_complete)

    def scrape_logged_in(self, close_on_complete = True):
        driver = self.driver
        _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@id='profile-xingid-container']")))
        profile_container = driver.find_element_by_xpath("//div[@id='profile-xingid-container']")
        _ = WebDriverWait(profile_container, 3).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.name =  ''.join([e.text for e in profile_container.find_elements_by_tag_name("h1")])

        # get interest
        try:
            _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='tab-content']")))
            iFrame = driver.find_element_by_xpath("//iframe[@title='tab-content']")
            driver.switch_to.frame(iFrame)
            int = driver.find_element_by_xpath('//div[@id="interests"]')
            for interest in int.find_elements_by_tag_name("li"):
                self.add_interest(Interest(interest.text.encode('utf-8').strip()))
        except:
            pass

		# get accomplishment
        try:
            _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="awards"]')))
            acc = driver.find_element_by_xpath('//div[@id="awards"]')
            for accomplishment in acc.find_elements_by_tag_name("li"):
                self.add_accomplishment(Accomplishment(accomplishment.text.encode('utf-8').strip()))
        except:
            pass

		# get organisation
        try:
            _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="organizations"]')))
            org = driver.find_element_by_xpath('//div[@id="organizations"]')
            for organisation in org.find_elements_by_tag_name("li"):
                self.add_organisation(Organisation(organisation.text.encode('utf-8').strip()))
        except:
            pass
            
		# get qualification
        try:
            _ = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="qualifications"]')))
            quali = driver.find_element_by_xpath('//div[@id="qualifications"]')
            for qualification in quali.find_elements_by_tag_name("li"):
                self.add_qualification(Qualification(qualification.text.encode('utf-8').strip()))
        except:
            pass
            
        if close_on_complete:
            driver.close()

    def __repr__(self):
        return "{name}\n\nInterest\n{int}\n\nAccomplishment\n{acc}\n\nOrganisation\n{org}\n\nQualification\n{quali}".format(name = self.name, int = self.interests, acc = self.accomplishments, org = self.organisations, quali = self.qualifications)

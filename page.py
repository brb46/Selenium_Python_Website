from locator import *
from element import BasePageElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import json
import time

with open("data.json", "w") as f:
    json.dump([],f)

def write_json(new_data,filename='data.json'):
    with open(filename, 'r+') as file:
        #First we load existing data into a dictionary.
        file_data = json.load(file)
        #Join new_data with file_data inside emp_details 
        file_data.append(new_data)
        #sets files current postion at offset.
        file.seek(0)
        #convert back to json
        json.dump(file_data,file, indent = 4)

class SearchTextElement(BasePageElement):
    locator = "q" #placeholder

class BasePage(object):
    def __init__ (self, driver):
        self.driver = driver 

class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_Matches(self):
        return "Python" in self.driver.title  #returns true if python is in the title 
    def click_go_Button(self):
        element = self.driver.find_element(*MainPageLocators.go_Button)
        element.click()
    def click_search_Button(self):
        element = self.driver.find_element(*MainPageLocators.search_Button)
        element.click()
    def click_psf_Tab(self):
        element = self.driver.find_element(*MainPageLocators.psf_Tab)
        element.click()
    def click_faq_Button(self):
        element = self.driver.find_element(*MainPageLocators.membershipFAQ_button)
        element.click()
    def click_donate_Button(self):
        element = self.driver.find_element(*MainPageLocators.doante_Button)
        element.click()
    def click_volunteer_Button(self):
        element = self.driver.find_element(*MainPageLocators.volunteer_Button)
        element.click()
    def click_sponsor_Button(self):
        element = self.driver.find_element(*MainPageLocators.sponsors_Button)
        element.click()
    def click_psf_grants_Button(self):
        element = self.driver.find_element(*MainPageLocators.psf_grant_Button)
        element.click()
    def click_docs_Button(self):
        element = self.driver.find_element(*MainPageLocators.docs_Tab)
        element.click()
    def click_newdocs_Button(self):
        element = self.driver.find_element(*MainPageLocators.newdoc_Button)
        element.click()
    def click_pypi_Tab(self):
        element = self.driver.find_element(*MainPageLocators.pypi_Tab)
        element.click()
    def click_Jobs_Tab(self):
        element = self.driver.find_element(*MainPageLocators.jobs_Tab)
        element.click()
    def click_community_Tab(self):
        element = self.driver.find_element(*MainPageLocators.community_Tab)
        element.click()
    
    def click_diversity_Page(self):
        element = self.driver.find_element(*MainPageLocators.diversity_page)
        element.click()

    def click_backend_jobPage(self):
        element1 = self.driver.find_element(*MainPageLocators.types_Tab)
        element2 = self.driver.find_element(*MainPageLocators.backend_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()
    
    def click_web_jobPage(self):
        element1 = self.driver.find_element(*MainPageLocators.types_Tab)
        element2 = self.driver.find_element(*MainPageLocators.web_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()
    
    def click_dataanalystPage(self):
        element1 = self.driver.find_element(*MainPageLocators.categories_Tab)
        element2 = self.driver.find_element(*MainPageLocators.dataanalyst_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()

    def click_otherPage(self):
        element1 = self.driver.find_element(*MainPageLocators.categories_Tab)
        element2 = self.driver.find_element(*MainPageLocators.other_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()

    def click_telecommutePage(self):
        element1 = self.driver.find_element(*MainPageLocators.locations_Tab)
        element2 = self.driver.find_element(*MainPageLocators.telecommute_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()

    def click_WilmingotonPage(self):
        element1 = self.driver.find_element(*MainPageLocators.locations_Tab)
        element2 = self.driver.find_element(*MainPageLocators.wilmington_Dropdown)
        hover = ActionChains(self.driver).move_to_element(element1)
        hover.perform()
        element2.click()

    
    
 
class psfPage(BasePage):
        def is_faqtitle_Matches(self):
            return "Membership FAQ" in self.driver.page_source
        def is_titlepage_Exists(self):
            try:
                item = self.driver.find_element(*MainPageLocators.PSF_section)
                print(item)
            except NoSuchElementException:
                return False
            return True
               
        def is_donatetitle_Matches(self):
            return "How to Contribute" in self.driver.page_source
        def is_volunteertitle_Matches(self):
            return "How to Volunteer" in self.driver.page_source
        def is_sponsortitle_Matches(self):
            return "Sponsorship Possibilities" in self.driver.page_source
        def is_sponsorpage_Matches(self):
            return "The Python Software Foundation Sponsorship Program" in self.driver.page_source
        def is_psfgrantstitle_Matches(self):
            return "Proposal Guidelines, FAQ and Examples" in self.driver.page_source
        
class docsPage(BasePage):
        def is_docsnumber_Matches(self):
            return "Python 3.11.4 documentation" in self.driver.page_source
        def is_versiontitle_Matches(self):
            return "What’s New In Python 3.11" in self.driver.page_source

    

class SearchResultPage(BasePage):
    def is_results_Found(self):
        return "No results found." not in self.driver.page_source  #if "no result found" is not in the page, returns true
    def is_result_on_SearchBar(self):
        return "pycon"  in self.driver.page_source    #returns true if pycon exists in searchbar after clicking it 
    
    
class SearchpypiPage(BasePage):  
    def resultlist(self):
        element = WebDriverWait (self.driver,10).until(EC.presence_of_element_located(
        ( By.CSS_SELECTOR,"[aria-label='Search results']")))
         
        lists = self.driver.find_elements( By.XPATH,'//a[@class="package-snippet"]')
        isNextDisabled = False
        page = 1

        while not isNextDisabled:
            try:
                lists = self.driver.find_elements( By.XPATH,'//a[@class="package-snippet"]')
                for list in lists:

                    title = list.find_element(By.CSS_SELECTOR,".package-snippet__name").text
                    version = list.find_element(By.CSS_SELECTOR, ".package-snippet__version").text
                    date = list.find_element(By.TAG_NAME, "time").text
            
                    Summary = list.find_element(By.CSS_SELECTOR, ".package-snippet__description").text
                    if Summary == "":
                        Summary = "Summary Not Found"
            
                    print(title)
                    print(version)
                    print(date)
                    print(Summary + "\n")  #prints out the information of the search results in the console 

                    write_json ({
                    "page": str(page),
                    "title": title,
                    "version": version,
                    "date": date,
                    "Summary": Summary,
                
            })

                next_Button = WebDriverWait (self.driver,10).until(EC.presence_of_element_located(
                    (By.XPATH,"//*[contains(text(), 'Next')]")))

                page += 1
                next_Class = next_Button.get_attribute('class')
                if 'button--disabled' in next_Class:
                    isNextDisabled = True
                else:
                    print("hi")
                    #next button is click until button-disabled is true
                    self.driver.find_element(By.XPATH, "//*[contains(text(), 'Next')]").click()        
            except Exception as e:
                print(e, "Main error")
                isNextDisabled = True

class jobsPage(BasePage):
    def is_backend_title_Matches(self):
         return "25 Python jobs in Back end" in self.driver.page_source
    def is_web_title_Matches(self):
        return "11 Python jobs in Web" in self.driver.page_source
    def is_dataanalyst_title_Matches(self):
        return "Data Analyst" in self.driver.page_source
    def is_other_title_Matches(self):
        return "3 Python jobs in Other" in self.driver.page_source
    def is_telecommute_title_Matches(self):
        return "Telecommute Jobs" in self.driver.page_source
    def is_wilmington_title_Matches(self):
        return "Wilmington, Delaware – United States" in self.driver.page_source

class communityPage(BasePage):
    def is_diversity_title_Matches(self):
        return "Diversity" in self.driver.page_source
    
    
    
    







            



    
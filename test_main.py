import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import page
import time
import json


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://www.python.org")
    
    def test_search_python(self):
         mainPage = page.MainPage(self.driver)
         assert mainPage.is_title_Matches()
         mainPage.search_text_element = "pycon"   #search pycon in searchbar
         mainPage.click_go_Button()
         search_result_page = page.SearchResultPage(self.driver) #initialize searchresultpage
         assert search_result_page.is_results_Found()
         assert search_result_page.is_result_on_SearchBar()

    def tearDown(self):
        print("passed")
        self.driver.close()

class PythonPSF(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://www.python.org")

    def test_membership_qaPage(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_psf_Tab()
        psfPage = page.psfPage(self.driver)
        assert psfPage.is_faqtitle_Matches()
        mainPage.click_faq_Button()
        assert psfPage.is_titlepage_Exists()
       


    def test_donatePage(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_psf_Tab()
        psfPage = page.psfPage(self.driver)
        assert psfPage.is_donatetitle_Matches()
        mainPage.click_donate_Button()
        assert psfPage.is_titlepage_Exists()
    
    def test_volunteerPage(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_psf_Tab()
        psfPage = page.psfPage(self.driver)
        assert psfPage.is_volunteertitle_Matches()
        mainPage.click_volunteer_Button()
        assert psfPage.is_titlepage_Exists()


    def test_sponsorsPage(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_psf_Tab()
        psfPage = page.psfPage(self.driver)
        assert psfPage.is_sponsortitle_Matches()
        mainPage.click_sponsor_Button()
        assert psfPage.is_sponsorpage_Matches()
        
    def test_psf_grants_program_Page(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_psf_Tab()
        psfPage = page.psfPage(self.driver)
        assert psfPage.is_psfgrantstitle_Matches()
        mainPage.click_psf_grants_Button()
        assert psfPage.is_titlepage_Exists()


    def tearDown(self):
        print("passed")
        self.driver.close()

class PythonDocs(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://www.python.org")

    def test_python_Doc(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_docs_Button()
        docsPage = page.docsPage(self.driver)
        assert docsPage.is_docsnumber_Matches()
    def test_python_newinfo_Doc(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_docs_Button()
        docsPage = page.docsPage(self.driver)
        assert docsPage.is_docsnumber_Matches()
        mainPage.click_newdocs_Button()
        assert docsPage.is_versiontitle_Matches()
    def tearDown(self):
        print("passed")
        self.driver.close()

class pythonPYPI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        browser = self.driver.get("https://www.python.org")

    def test_python_searchbarPYPI (self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_pypi_Tab()
        mainPage.search_text_element = "pentagon"
        pypiPage = page.SearchpypiPage(self.driver)
        mainPage.click_search_Button()
        pypiPage.resultlist()
        
        time.sleep(3)

    def tearDown(self):
        print("passed")
        self.driver.close()

class pythonJobs(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.get("https://www.python.org")


    def test_python_BackendJob(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_backend_jobPage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_backend_title_Matches()
    
    def test_python_webJob(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_web_jobPage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_web_title_Matches()
    
    def test_python_dataAnalyst(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_dataanalystPage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_dataanalyst_title_Matches()

    def test_python_Other(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_otherPage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_other_title_Matches()

    def test_python_Telecommute(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_telecommutePage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_telecommute_title_Matches()
        
    
    def test_python_Wilmington(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_Jobs_Tab()
        mainPage.click_WilmingotonPage()
        typepage = page.jobsPage(self.driver)
        assert typepage.is_wilmington_title_Matches()
        
    def test_python_Community(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_Matches()
        mainPage.click_community_Tab()
        mainPage.click_diversity_Page()
        typepage = page.communityPage(self.driver)
        assert typepage.is_diversity_title_Matches()
        

    
       
    def tearDown(self):
        print("passed")
        self.driver.close()
       
if __name__ == '__main__':
    unittest.main()


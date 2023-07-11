from selenium.webdriver.common.by import By

class MainPageLocators(object):
    go_Button = (By.ID, "submit")
    search_Button = (By.CLASS_NAME, "fa.fa-search")
    psf_Tab = (By.CLASS_NAME, "psf-meta")  
    membershipFAQ_button = (By.XPATH,"//a[contains(text(), 'Membership')]")
    PSF_section = (By.XPATH,'//h1[@class="page-title"]')
    doante_Button = (By.XPATH,"//a[contains(text(), 'How to Contribute')]")
    volunteer_Button = (By.XPATH,"//a[contains(text(), 'How to Volunteer')]")
    sponsors_Button = (By.XPATH, '//a[text()="Sponsorship Possibilities"]')
    psf_grant_Button =(By.XPATH, '//a[text()="Proposal Guidelines, FAQ and Examples"]')          
    docs_Tab =(By.CLASS_NAME,"docs-meta")
    newdoc_Button = (By.XPATH,'//a[@href="whatsnew/3.11.html"]')
    pypi_Tab =(By.CLASS_NAME, "pypi-meta")
    jobs_Tab = (By.CLASS_NAME,"jobs-meta")
    types_Tab = (By.XPATH,'//a[@href="/jobs/types/"]')
    backend_Dropdown = (By.XPATH, '//a[text()="Back end"]')
    web_Dropdown = (By.XPATH, '//a[text()="Web"]')
    categories_Tab = (By.XPATH,'//a[@href="/jobs/categories/"]' )
    dataanalyst_Dropdown = (By.XPATH,'//a[@href="/jobs/types/"]')
    other_Dropdown = (By.XPATH, '//a[@href="/jobs/category/other/"]' )
    locations_Tab = (By.XPATH, '//a[@href="/jobs/locations/"]')
    telecommute_Dropdown = (By.XPATH, '//a[@href="/jobs/location/telecommute/"]')    
    wilmington_Dropdown = (By.XPATH, '//a[@href="/jobs/location/wilmington-delaware-united-states/"]')                    
    community_Tab = (By.XPATH, '//a[@href="/community-landing/"]')
    diversity_page =(By.XPATH,'//a[@href="/community/diversity"]')
    

    

class SearchResultsPageLocators(object):
    searchbarText = (By.CSS_SELECTOR, '[value ="pycon"]')
       
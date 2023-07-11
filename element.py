from selenium import*
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By 

class BasePageElement(object):
    locator = "q"
    def __set__(self,obj,value):        #obj = mainpage , Ex: value = 5
        driver = obj.driver
        WebDriverWait(driver,100).until(
        lambda driver: driver.find_element(By.NAME,self.locator))  #locator = q
        driver.find_element(By.NAME,self.locator).clear()
        driver.find_element(By.NAME,self.locator).send_keys(value)
    
    def __get__(self, obj,owner):
        driver = obj.driver
        WebDriverWait(driver,100).until(
        lambda driver: driver.find_element(By.NAME,self.locator))
        element = driver.find_element(By.NAME,self.locator)
        return element.get_attribute("value")
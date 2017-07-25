'''
Created on Jul 21, 2017

@author: compass
'''
from selenium.webdriver.common.by import By

class AmazonDashboardPageLocator(object):
    
    amazonLogo=(By.CSS_SELECTOR, "#navbar .nav-logo-base")
   
    headerText=(By.CSS_SELECTOR, "#nav-xshop .nav-a")
    
    shopyByCategoryArrowIcon= (By.CSS_SELECTOR, "#nav-link-shopall .nav-arrow")
    
    amazonPrimeVideoText=(By.XPATH ,"//h2[text()='Amazon Prime Video']")
    
    searchFirstOption=(By.ID , "issDiv0")
    
    searchTextBox=(By.ID, "twotabsearchtextbox")
    
    
class SearchResultPageLocator(object):
    
    searchResultText=(By.CSS_SELECTOR, "#bcKwText>span")
    
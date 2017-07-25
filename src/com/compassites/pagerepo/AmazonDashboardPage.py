'''
Created on 21-Jul-2017

@author: Pooja Gadekar
'''
from src.com.compassites.properties.Locator import AmazonDashboardPageLocator
from src.com.compassites.properties.Locator import SearchResultPageLocator
from src.com.compassites.basepagerepo.element import BasePageElement

class BasePage(BasePageElement):
    def __init__(self, driver):
        self.driver = driver

class DashboardPage(BasePage):

    def is_title_matches(self):
        return "Amazon.in" in self.driver.title
    
    def verify_amazon_logo(self):
        return self.driver.find_element(*AmazonDashboardPageLocator.amazonLogo).is_displayed()
    
    def verify_listOfHeaderMenus(self):
        return  
    
    def text_amazonPromoVideo(self):
        return self.driver.find_element(*AmazonDashboardPageLocator.amazonPrimeVideoText).text
    
    def click_shopByCategoryArrowIcon(self):
        self.driver.find_element(*AmazonDashboardPageLocator.shopyByCategoryArrowIcon).click()
        
    def sendkeys_search_textbox(self,data):
        self.driver.find_element(*AmazonDashboardPageLocator.searchTextBox).send_keys(data)
      
    def click_firstSearchedOption(self):
        self.driver.find_element(*AmazonDashboardPageLocator.searchFirstOption).click()  
         
class SearchResultsPage(BasePage):
        
    def text_searchedResultText(self):
        return self.driver.find_element(*SearchResultPageLocator.searchResultText).text.replace("\"", "");
    
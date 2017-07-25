'''
Created on Jul 21, 2017

@author: compass
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

class Generic(object):
    
    def openBrowser(self,browserName,platform,selenium_grid_url):
        if browserName == "FIREFOX" :
            capabilities = DesiredCapabilities.FIREFOX.copy()
            capabilities['platform'] = platform
            
        elif  browserName == "CHROME" :
            capabilities = DesiredCapabilities.CHROME.copy()
            capabilities['platform'] = platform
           
        elif browserName == "IE" :
            capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            capabilities['platform'] = platform
            
        self.driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)
             
        self.driver.implicitly_wait(10)
        self.driver.maximize_window();
        
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
        

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True
    
    def scrollDown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        
    
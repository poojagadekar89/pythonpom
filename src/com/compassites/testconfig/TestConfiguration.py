'''
Created on Jul 21, 2017

@author: compass
'''
from  src.com.compassites.utils.Event import Generic
import configparser
import unittest, sys

class TestConfiguration(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        '''config = configparser.RawConfigParser()
        config.read("/Users/compass/Documents/python/pythonGenericPOM"+"Config.properties")'''
        selenium_grid_url = "http://192.168.3.179:5555/wd/hub"
        Generic.openBrowser(inst, "CHROME", "MAC", selenium_grid_url)
        # Create a desired capabilities object as a starting point.
        '''self.driver = webdriver.Firefox()'''
        inst.driver.get("http://www.amazon.in/")
      
    def tearDown(self):
        '''if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
        super(TestConfiguration, self).tearDown()  '''
        type, value, traceback = sys.exc_info()
        if type is AssertionError:
            self.driver.save_screenshot(r'screenshot-failure.png')
        elif type is Exception() :
            self.driver.save_screenshot(r'screenshot-error.png')

        
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
        

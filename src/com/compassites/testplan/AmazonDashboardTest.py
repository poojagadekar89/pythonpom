'''
Created on 21-Jul-2017

@author: Pooja Gadekar
'''
import unittest
from src.com.compassites.pagerepo.AmazonDashboardPage import DashboardPage
from src.com.compassites.pagerepo.AmazonDashboardPage import SearchResultsPage
import time
from src.com.compassites.testconfig.TestConfiguration import TestConfiguration
from src.com.compassites.suiteNames import TestRunner


class AmazonDashboardTest(TestConfiguration):
    '''Verify amazon dashboard items'''
    def test_verifyAmazonDashboardPageFunctionality(self):
        dashboard_page = DashboardPage(self.driver)
        self.assertTrue(dashboard_page.is_title_matches(),"Amazon.in title doesn't match.")
        self.assertTrue(dashboard_page.verify_amazon_logo(), "Amazon Logo not available on web page")
        
        dashboard_page.click_shopByCategoryArrowIcon()
        self.assertEqual(dashboard_page.text_amazonPromoVideo(), "Amazon Prime Video", "Actual & Expected value not Matched")
        
    '''Verify amazon search action functionality'''    
    def test_verifySearchPageFunctionality(self):
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.sendkeys_search_textbox("shoes")
        time.sleep(3);
        dashboard_page.click_firstSearchedOption();
        
        search_page = SearchResultsPage(self.driver)
        self.assertEqual(search_page.text_searchedResultText(), "shoes1234", "Actual & Expected value not Matched")
    
'''if __name__ == "__main__":
    
    directoryName = os.getcwd()
    outfile = open("SeleniumPythonTestSummary.html", "w")
    # configure HTMLTestRunner options
    runner = TestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
    TestRunner.main()'''
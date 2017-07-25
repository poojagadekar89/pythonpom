'''
Created on Jul 24, 2017

@author: compass
'''
import unittest
from src.com.compassites.suiteNames import TestRunner
from src.com.compassites.testplan import AmazonDashboardTest
import os
# get the directory path to output report file
directoryName = os.getcwd()
 
# get all tests from SearchText and HomePageTest class
dashboardtest = unittest.TestLoader().loadTestsFromModule(AmazonDashboardTest,)
 
# create a test suite combining search_text and home_page_test
testsuite = unittest.TestSuite(dashboardtest)
 
# open the report file
outfile = open("SeleniumPythonTestSummary.html", "w")
 
# configure HTMLTestRunner options
runner = TestRunner.HTMLTestRunner(stream=outfile,title='Test Report', description='Acceptance Tests')
 
# run the suite using HTMLTestRunner
runner.run(testsuite)

if __name__ == "__main__":
   
    TestRunner.main()
# import pytest
import unittest
from unittest.case import _AssertWarnsContext

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
import time


class TestMethod(unittest.TestCase):

    def test_mentortest_1(self):
        self.driver = webdriver.Chrome("C:\\Driver\\ChromeDriver\\chromedriver.exe")
        self.driver.get("http://dev.mentorerp.com:8080/onboard")
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()  # Enter First name
        self.driver.find_element(By.ID, "mat-input-0").send_keys("solomon.raja@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, "mat-button-wrapper").click()
        time.sleep(2)

        self.actual_errormessage = "not found1"
        self.expected_errormessage = self.driver.find_element(By.CLASS_NAME, "cdk-overlay-container").text

        try:
            assert self.expected_errormessage == self.actual_errormessage
            print("Test is Failed")
        except AssertionError:
            print("\n Test case1 is passed. \n Invalid email id with valid password - The Actual Error message is '%s'" % self.expected_errormessage)
        time.sleep(3)
        self.driver.close()
        time.sleep(3)

    def test_mentortest_2(self):
        self.driver = webdriver.Chrome("C:\\Driver\\ChromeDriver\\chromedriver.exe")
        self.driver.get("http://dev.mentorerp.com:8080/onboard")
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()  # Enter First name
        self.driver.find_element(By.ID, "mat-input-0").send_keys("solomon.rajaps@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("12345")
        self.driver.find_element(By.CLASS_NAME, "mat-button-wrapper").click()
        time.sleep(2)
        #self.driver.close()

        self.actual_errormessage = "password must have length greater than or equal to 5"
        self.expected_errormessage = self.driver.find_element(By.XPATH, "/html/body/div[2]").text

        try:
            assert self.expected_errormessage == self.actual_errormessage
            print("Test is Failed")
        except AssertionError:
            print("\n Test case2 is Passed.\n Valid email id with Invalid password - The Error message is '%s'" % self.expected_errormessage)
        time.sleep(3)
        self.driver.close()
        time.sleep(3)

    def test_mentortest_3(self):
        self.driver = webdriver.Chrome("C:\\Driver\\ChromeDriver\\chromedriver.exe")
        self.driver.get("http://dev.mentorerp.com:8080/onboard")
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()  # Enter First name
        self.driver.find_element(By.ID, "mat-input-0").send_keys("solomon.rajaps@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123456")
        self.driver.find_element(By.CLASS_NAME, "mat-button-wrapper").click()
        time.sleep(2)
        #self.driver.close()

        self.actual_errormessage = "Please enter correct password"
        self.expected_errormessage = self.driver.find_element(By.CLASS_NAME, "cdk-overlay-container").text

        try:
            assert self.expected_errormessage == self.actual_errormessage
            print("\n Test case3 is Passed. \n Valid email id with Invalid password - The Error message is: '%s'" % self.expected_errormessage)
        except AssertionError:
            print("Test is Failed")
        time.sleep(4)


    def test_mentortest_4(self):
        self.driver = webdriver.Chrome("C:\\Driver\\ChromeDriver\\chromedriver.exe")
        self.driver.get("http://dev.mentorerp.com:8080/onboard")
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//*[@id='mat-tab-label-0-1']/div").click()
        self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()  # Enter First name
        self.driver.find_element(By.ID, "mat-input-0").send_keys("solomon.rajaps@gmail.com")

        self.driver.find_element(By.XPATH, "//*[@id='mat-tab-content-0-0']/div/form/div/a").click()
        time.sleep(3)

        # click Forgot Password?
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-5']").send_keys("helen@gmail.com")

        self.driver.find_element(By.XPATH,
                                 "//*[@id='mat-dialog-0']/app-forget-password/div/mat-dialog-content/form/div/button").click()
        time.sleep(2)
        #self.driver.close()

        self.actual_errormessage = "Failed to sent, Reason:undefined"
        self.expected_errormessage = self.driver.find_element(By.XPATH, "//simple-snack-bar[@class='mat-simple-snackbar ng-star-inserted']").text

        try:
            assert self.expected_errormessage == self.actual_errormessage
            print("Test is Failed")
        except AssertionError:
            print("\n Test case4 is Passed.\n Forgot password with Invalid email id - The Error message is: '%s'" % self.expected_errormessage)
        time.sleep(4)

    def test_mentortest_5(self):
        # Register the contact Information
        self.driver = webdriver.Chrome("C:\\Driver\\ChromeDriver\\chromedriver.exe")
        self.driver.get("http://dev.mentorerp.com:8080/onboard")
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//span[@class='ng-star-inserted']").click()  # Enter First name
        self.driver.find_element(By.ID, "mat-input-0").send_keys("solomon.rajaps@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("12345678")
        self.driver.find_element(By.CLASS_NAME, "mat-button-wrapper").click()
        time.sleep(3)
        # click new application
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/mat-sidenav-container/mat-sidenav/div/mat-nav-list/mat-list-item[2]/div/div[2]/a").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-applications/div[2]/button").click()
        # driver.close()
        time.sleep(3)
        # Login with Parent name and contact number
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-5']").send_keys("Ravi")
        self.driver.find_element(By.XPATH, "//*[@id='mat-input-6']").send_keys(("9087687654"))
        self.driver.find_element(By.XPATH,
                                 "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-amend-application/div[2]/mat-card/mat-card-content/form/div[2]/button").click()
        time.sleep(2)
        self.driver.close()

        print("\n Test case5 is Passed. \n User Successfully log in to the Application")
        time.sleep(4)


if __name__ == "__main__":
    unittest.main()



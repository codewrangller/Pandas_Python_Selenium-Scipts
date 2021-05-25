from selenium import webdriver
from selenium.webdriver.support.ui import Select
import codecs
import os
import time
import pdfkit
import getpass

class Payslips:
    """This class generates bulk html from web_app using selenium"""

    def navigation(self):
        #This function navigates through the web_app using selenium
        
        browser = webdriver.Chrome('chromedriver.exe')
        self.nav = browser
        browser.get(#'url address')
        email = browser.find_element_by_id('Email')
        email.send_keys(#'username/email')
        password = browser.find_element_by_id('Password')
        pass_word = getpass.getpass(prompt='User, enter your password:')
        password.send_keys(pass_word)
        password.submit()
        browser.find_element_by_xpath("""/html/body/div[1]/div[2]/nav/ul/li[10]/a/i""").click()
        element_zero = browser.find_element_by_xpath("""/html/body/div[1]/div[2]/nav/ul/li[10]/ul/li[4]/a""")
        browser.execute_script("arguments[0].click();", element_zero)
        element = browser.find_element_by_xpath("""/html/body/div[1]/div[2]/nav/ul/li[10]/ul/li[4]/ul/li[2]/a""")
        browser.execute_script("arguments[0].click();", element)
        element_one = browser.find_element_by_xpath("""//*[@id="heading_1"]/table/tbody/tr/td[2]/button""")
        browser.execute_script("arguments[0].click();", element_one)
        element_two = browser.find_element_by_xpath("""//*[@id="collapse_1"]/div/table/tbody/tr[4]/td[2]/a""")
        browser.execute_script("arguments[0].click();", element_two)
        new_locations = browser.find_elements_by_id("location")
        for new_location in new_locations:
            print(new_location.text)
        
    
    def spool_html(self):
        #This function generates bulk html for all specified locations
        
        for x in range(1, 21):
            value = str(x)
            select = Select(self.nav.find_element_by_xpath("""//*[@id="location"]"""))
            select.select_by_value(value)
            select = Select(self.nav.find_element_by_xpath("""//*[@id="action"]"""))
            select.select_by_value('html')
            html_file = self.nav.find_element_by_xpath("""//*[@id="processButon"]""")
            self.nav.execute_script("arguments[0].click();", html_file)
            time.sleep(5)
            Places = {'1':'LEKKI'...........'20': 'OJO'}
            if value in Places.keys():
                tool = Places[f'{value}']
            completeName=os.path.join(f"C:\\your_path\\{tool}.html")
            file_object = codecs.open(completeName, "w", "utf-8")
            html = self.nav.page_source
            file_object.write(html)
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            options = {'encoding':'utf-8'}
            pdfkit.from_file(f"C:\\your_path\\{tool}.html", f'C:\\new_path\\{tool}.pdf', configuration=config, options=options) 
            self.nav.back()

p = Payslips()
p.navigation()
p.spool_html()

        
        
        
        


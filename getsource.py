
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver
import time
import sys
import os
from methods_json import load_json, write_json
from termcolor import colored, cprint

import datetime
import random
import json

def getDate():
    x = datetime.datetime.now()
    year = x.strftime("%Y")
    month = x.strftime("%m")
    day = x.strftime("%d")
    timestamp = str(year) + "-"+month + "-"+ day
    return timestamp

class GetSource:
    def __init__(self):
        self.URL_link_quote = "https://www.brainyquote.com/quote_of_the_day"
        self.URL_link_word = "https://www.dictionary.com/e/word-of-the-day/"
        self.quotesDB = load_json("template_quotes.json")
        self.wordDB = load_json("template_word.json")

    def openBrowser(self):
            # selenium
            options = Options()
            options.add_argument("--headless")

            cprint("\n[*] Opening Firefox", 'cyan')
            try:
                self.driver = webdriver.Firefox(options=options)
            except Exception as e:
                try:
                    print(e)
                    cprint("[!] Open on Windows", 'cyan')
                    binary = FirefoxBinary(
                        "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                    self.driver = webdriver.Firefox(
                        firefox_binary=binary, executable_path=r"C:\\geckodriver.exe", options=options)
                except Exception as e:
                    try:
                        print(e)
                        cprint("[!] Open on Linux", 'cyan')
                        self.driver = webdriver.Firefox(
                            executable_path='geckodriver/geckodriver')
                    except Exception as e:
                        try:
                            print(e)
                            cprint("[!] Trying open last chance", 'cyan')
                            self.driver = webdriver.Firefox(
                                executable_path='geckodriver\\geckodriver')
                        except Exception as e:
                            print("!!! ERROR: " + str(e), 'red')
                            sys.exit()
            self.driver.set_window_position(0, 0)
            self.driver.set_window_size(100, 100)

    def main(self):
        self.openBrowser()
        self.getWord()
        self.getQuotes()
        self.driver.close()
        self.driver.quit()

    def getWord(self):
        cprint("[!] getWord Opening URL", 'blue')
        
        self.wordDB["date"] = getDate()

        self.driver.get(self.URL_link_word)
        time.sleep(5)

        self.wordDB["word"] = self.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[3]/h1").text
        self.wordDB["sound"] = self.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[4]/div/a").get_attribute("href")
        self.wordDB["type"] = self.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/div/p[1]/span/span").text
        self.wordDB["mean"] = self.driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[5]/div/p[2]").text
        print(self.wordDB)

        write_json("wordoftheday.json",self.wordDB)

    def getQuotes(self):
        cprint("[!] getQuotes Opening URL", 'blue')
        
        self.quotesDB["date"] = getDate()

        self.driver.get(self.URL_link_quote)
        time.sleep(5)

        self.quotesDB["quotes"][0]["quote"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div/div/a[1]/div").text
        self.quotesDB["quotes"][0]["author"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[2]/div/div/div/a[2]").text

        self.quotesDB["quotes"][1]["quote"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[3]/div/div/a[1]/div").text
        self.quotesDB["quotes"][1]["author"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[3]/div/div/a[2]").text

        self.quotesDB["quotes"][2]["quote"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[4]/div/div/a[1]/div").text
        self.quotesDB["quotes"][2]["author"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[4]/div/div/a[2]").text

        self.quotesDB["quotes"][3]["quote"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[5]/div/div/a[1]/div").text
        self.quotesDB["quotes"][3]["author"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[5]/div/div/a[2]").text

        self.quotesDB["quotes"][4]["quote"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[7]/div/div/a[1]/div").text
        self.quotesDB["quotes"][4]["author"] = self.driver.find_element_by_xpath("/html/body/main/div[1]/div[7]/div/div/a[2]").text

        random.shuffle(self.quotesDB["quotes"])

        write_json("quotes.json",self.quotesDB)
        
        print(json.dumps(self.quotesDB, indent=1))

if __name__ == "__main__":
    gs = GetSource()
    gs.main()

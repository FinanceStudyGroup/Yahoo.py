#!/usr/bin/python
# ------------------------------------------------------------------------------
# Yahoo Finance Launcher
# ------------------------------------------------------------------------------

# Import required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ------------------------------------------------------------------------------
Ticker = raw_input("Ticker: ")
# ------------------------------------------------------------------------------

driver = webdriver.Chrome()

# Link to the profile page
YahooFinanceProfile = ("https://finance.yahoo.com/quote/"+Ticker+"/profile?p="+Ticker)

# Locate Reuters company profile page
driver.get(YahooFinanceProfile)
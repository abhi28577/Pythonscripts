#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:21:20 2018

@author: abhi28577
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Safari()
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://www.rediff.com")

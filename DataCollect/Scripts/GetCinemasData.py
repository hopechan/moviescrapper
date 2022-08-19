import json
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# import By
from selenium.webdriver.common.by import By

URL_BASE = 'https://cinemas.com.ni/cartelera/'
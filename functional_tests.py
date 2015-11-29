import pdb
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

pdb.set_trace()

assert 'Django' in browser.title
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

# driver = webdriver.Chrome('/Users/zachariah/internship!/chromedriver')
#
url = "https://commons.wikimedia.org/wiki/Category:Nazi_concentration_camps_by_name"
# driver.get(url)

# links = driver.find_elements_by_xpath("//a[@href]")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
links = soup.find_all('a')
i = 0
for link in links:
	if i == 18:
		print(link)
		print(link.get('href'))
		url = "https://commons.wikimedia.org/%s"%(link.get('href'))
		r = requests.get(url)
		soup = BeautifulSoup(r.content, 'lxml')
		# print(url)
		location = soup.findAll('th')
		# print(location)
		print(location[1].findNext('td'))
		# print(location[1].findAll('a'))
	i += 1

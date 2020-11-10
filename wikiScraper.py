from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import csv

url = "https://commons.wikimedia.org/wiki/Category:Nazi_concentration_camps_by_name"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml')
links = soup.find_all('a')
i = 0
locationFound = False
name = None

with open('spreadsheet.csv', 'w', newline='') as csvfile:
	fieldnames = ['Camp', 'Location']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()

	for link in links:
		if i >= 4 and i < 98:
			url = "https://commons.wikimedia.org/%s"%(link.get('href'))
			r = requests.get(url)
			soup = BeautifulSoup(r.content, 'lxml')
			info = soup.findAll('th')
			for category in info:
				if category.text == "Location":
					locations = category.findNext('td')
					for location in locations.findAll('a'):
						name = location.text
			if not name:
				name = 'N/A'
			writer.writerow({'Camp': link.text, 'Location': name})
			name = None
		i += 1

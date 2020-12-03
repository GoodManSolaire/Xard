import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import csv
import re

def scrap_data(driver,cardName,cardPrice,cardListing):
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	rvalues = soup.find_all("div", {"id":"primary"})

	for rvalue in rvalues:
		cardName.append(rvalue.find("h2", {"class":"woocommerce-loop-product__title"}).get_text().strip())
		cardPrice.append(rvalue.find("span", {"price"}).get_text().strip())
		cardListing.append(rvalue.find("small", {"class":"wcvendors_sold_by_in_loop"}).get_text().strip())

def baseballXard():
	PATH = "C:\Program Files (x86)\chromedriver.exe"
		
	options = Options()
	options.add_argument("window-size=1400,600")

	

	options.add_argument(f'user-agent={user_agent}')
	driver = webdriver.Chrome(PATH, options=options)
		
	cardName = []
	cardPrice = []
	cardListing = []

	file = open('output.csv', 'w')
	writer = csv.writer(file)

	for i in range(1,7):
		url = "https://www.tradingcardexchange.com/product-category/sports/baseball/page/"+str(i)
		driver.get(url)
		search = driver.find_elements_by_class_name("products")
		for i in search:
			print(i.text)
			print('\n')	
		scrap_data(driver,cardName,cardPrice,cardListing)
		print("Baseball Page " + driver.title + " End")	
	print("Baseball Fin")
	driver.quit()

def basketballXard():
	PATH = "C:\Program Files (x86)\chromedriver.exe"
		
	options = Options()
	options.add_argument("window-size=1400,600")

	ua = UserAgent()
	a = ua.random
	user_agent = ua.random

	options.add_argument(f'user-agent={user_agent}')
	driver = webdriver.Chrome(PATH, options=options)
		
	cardName = []
	cardPrice = []
	cardListing = []

	file = open('output.csv', 'w')
	writer = csv.writer(file)

	for i in range(1):
		url = "https://www.tradingcardexchange.com/product-category/sports/basketball/"
		driver.get(url)
		search = driver.find_elements_by_class_name("products")
		for i in search:
			print(i.text)
			print('\n')	
		scrap_data(driver,cardName,cardPrice,cardListing)
		print("Basketball Page " + driver.title + " End")
	print("Basketball FIN")
	driver.quit()

def footballXard():
	PATH = "C:\Program Files (x86)\chromedriver.exe"
		
	options = Options()
	options.add_argument("window-size=1400,600")

	ua = UserAgent()
	a = ua.random
	user_agent = ua.random

	options.add_argument(f'user-agent={user_agent}')
	driver = webdriver.Chrome(PATH, options=options)
		
	cardName = []
	cardPrice = []
	cardListing = []

	file = open('output.csv', 'w')
	writer = csv.writer(file)

	for i in range(1,5):
		url = "https://www.tradingcardexchange.com/product-category/sports/football/page/"+str(i)
		driver.get(url)
		search = driver.find_elements_by_class_name("products")
		for i in search:
			print(i.text)
			print('\n')	
		scrap_data(driver,cardName,cardPrice,cardListing)
		print("Football Page " +driver.title + " End")
	print("Football FIN")
	driver.quit()

def hockeyXard():
	PATH = "C:\Program Files (x86)\chromedriver.exe"
		
	options = Options()
	options.add_argument("window-size=1400,600")

	ua = UserAgent()
	a = ua.random
	user_agent = ua.random

	options.add_argument(f'user-agent={user_agent}')
	driver = webdriver.Chrome(PATH, options=options)
		
	cardName = []
	cardPrice = []
	cardListing = []

	file = open('output.csv', 'w')
	writer = csv.writer(file)

	for i in range(1):
		url = "https://www.tradingcardexchange.com/product-category/sports/hockey/"
		driver.get(url)
		search = driver.find_elements_by_class_name("products")
		for i in search:
			print('\n')
			print(i.text)
			print('\n')	
		scrap_data(driver,cardName,cardPrice,cardListing)
		print("Hockey Page " +driver.title + " End")
	print("Hockey FIN")
	driver.quit()

def psaSports():
	PATH = "C:\Program Files (x86)\chromedriver.exe"
		
	options = Options()
	options.add_argument("window-size=1400,600")

	ua = UserAgent()
	a = ua.random
	user_agent = ua.random

	options.add_argument(f'user-agent={user_agent}')
	driver = webdriver.Chrome(PATH, options=options)


	for i in range(1,100):
		url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=sports+trading+cards&_sacat=0&LH_TitleDesc=0&rt=nc&Professional%2520Grader=Professional%2520Sports%2520%2528PSA%2529&_dcat=212&_pgn="+str(i)
		driver.get(url)
		search = driver.find_elements_by_class_name("s-item")
		for i in search:
			print(i.text.strip())
			print('\n')	
		print("Ebay PSA " + driver.title + " End")	
	print("Ebay PSA FIN")
	driver.quit()

if __name__ == '__main__':
	baseballXard()
	basketballXard()
	footballXard()
	hockeyXard()
	psaSports()


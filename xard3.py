import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
import time
import random


cardName = [] #Card Name Column
cardPrice = [] #Card Price Column
cardListing = [] # Card Listing Column


def ebayReg():
	for i in range(1,5): #From Page 1 to Page x
		print("Page " + str(i) + " Complete") #Prints when page is finished scraping
		#delays = [4, 2, 6, 10, 12]
		#delay = random.choice(delays)
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
		url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=sports+trading+cards&_sacat=0&LH_TitleDesc=0&Professional%2520Grader=Professional%2520Sports%2520%2528PSA%2529&_dcat=212&_ipg=200&_pgn='+str(i)
		r = requests.get(url, headers=headers)
		data = r.text
		soup = BeautifulSoup(data, 'html.parser')
		productMain = soup.find('div', attrs={'class': 'srp-river'})
		for product in productMain:
			items = product.find_all('li', attrs={'class': 's-item'})
			for item in items:
				title = item.find('h3', attrs={'class': 's-item__title' })
				price = item.find('span', attrs={'class': 's-item__price' })
				listing = item.find('div', attrs={'class': 's-item__subtitle' })
				if title is not None:
					headline = title.get_text()
					cardName.append(headline)
				if price is not None:
					priceCard = price.get_text()
					cardPrice.append(priceCard)
				if listing is not None:
					listingCard = listing.get_text()
					cardListing.append(listingCard)
	content = {'cards': ({"Card Name":cardName, "Card Price":cardPrice})}
	df = pd.DataFrame.from_dict(content['cards'])
	df.transpose
	df.to_csv('ebay.csv', index=False, encoding='utf-8')#Outputs Data to excel file

if __name__ == "__main__":
	ebayReg()

#https://www.ebay.com/sch/i.html?_from=R40&_nkw=sports+trading+cards&_sacat=0&LH_TitleDesc=0&Professional%2520Grader=Professional%2520Sports%2520%2528PSA%2529&_dcat=212&rt=nc&_pgn=4
#https://www.ebay.com/sch/i.html?_from=R40&_nkw=sports+trading+cards&_sacat=0&LH_TitleDesc=0&Professional%2520Grader=Professional%2520Sports%2520%2528PSA%2529&_dcat=212&_pgn=5
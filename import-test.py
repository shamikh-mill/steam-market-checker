# http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests
import pandas as pd


page = requests.get('http://store.steampowered.com/search/?')  #retrieve webpage
tree = html.fromstring(page.content) # save rerults to a tree 

#This will create a list of buyers:
buyers = tree.xpath('//span[@class="title"]/text()')
#This will create a list of prices
prices = tree.xpath('//div[@class="col search_price discounted responsive_secondrow"]/text()')

print ('Buyers: ', buyers)
print ('Prices: ', prices) 

df = pd.DataFrame({'Buyer Name' : pd.Series(buyers), 
					'Price' : pd.Series(prices)}) 
print (df)
from bs4 import BeautifulSoup as bs 
import requests as req 
import time
url = 'https://news.google.com/'
def headlines():
	page = req.get(url)
	soup = bs(page.text,'html.parser')
	# txt = soup.prettify()
	# file = open('data.txt','w')
	# file.write(txt)
	div = soup.find_all('a',{'class':'DY5T1d'})
	for hf in div:
		print(hf.get_text())
headlines()	
# xBbh9

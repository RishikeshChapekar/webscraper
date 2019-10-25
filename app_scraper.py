import requests as req 
from bs4 import BeautifulSoup as bs 
trail = "play.google.com"
def names():
	url = "https://play.google.com/store/apps?hl=en"
	apps = req.get(url)
	soup = bs(apps.text,'html.parser')
	names = soup.find_all('div',{'class':"WsMG1c nnK0zc"})
	for i in names:
		print(i.text)
names()

#extracting matchups for NBA games happening today

from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
from urllib.request import urlopen
import urllib
import re

decoder_type = "utf-8"


#hard code our url but can be removed to be more flexible as development progresses
def parse_NBA(url = "https://www.espn.com"):
	
	#nav espn for the NBA link
	try:
		#nba_page = urlopen(url)
		with urlopen(url) as nbapage:
			soup = BeautifulSoup(nbapage,'lxml',from_encoding = 'utf-8')
	except urllib.error.HTTPError as e:
		print(e)
	except urllib.error.URLError as u:
		print(u)
	#diagnose(soup)
	#print(soup.get_text())
	#find_all picks up all tags with 'a' / hyperlink we  narrow it down for NBA to exist in the tagline somewhere
	#we can treat .Tag as dictionaries i is a tag object we can get the links via .get('href')
	tmp = soup.find_all("a", string="NBA")
	for i in soup.find_all('a'):
		if i.get('href') == '/nba/':
			return url + i.get('href')
	return ""

#refactor a bit to make finding specific href more flexible

#process get soup of our main starting site

def starting_soup(site_URL):
	try:
		with urlopen(site_URL) as espn_nba:
			soup = BeautifulSoup(espn_nba, 'lxml')
	except urllib.error.HTTPError as e:
		print(e)
	except urllib.error.URLerror as u:
		print(u)

	return soup

def final_endpt(soup,target):
	#expand for crawl or user input later (?)
	target = "https//www.espn.com/nba/scoreboard"
	t = BeautifulSoup(urlopen("https://www.espn.com/nba"),'lxml')
	oops = t.find_all('a')
	for items in oops:
		print(items.get('href'))
def main():
	url = "https://www.google.com"
	soup = starting_soup(url)
	final_endpt(soup,"")
	#we can add user input to pick which link they want to follow but for now aiming to get to NBA->Schedule or Scoreboard

main()

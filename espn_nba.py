#extracting matchups for NBA games happening today
import urllib
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
from urllib.request import urlopen
from urllib import robotparser
import re
decoder_type = "utf-8"

'''
function : parse_NBA()
********************************
@param url : the url of the NBA site
TODO: make this more flexible
'''
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

'''
function: allow_robot(pURL, url_Path)
************************************************
@param pURL : parent URL to access main site
@param url_Path : path we want to access no url only ./X/Y/Z etc
'''
def allow_robot(pURL):
	robot = robotparser.RobotFileParser()
	robot.set_url(pURL+"robots.txt")
	robot.read()
	return robot
#refactor a bit to make finding specific href more flexible

#process get soup of our main starting site

def starting_soup(site_URL):
	try:
		with urlopen(site_URL) as espn_nba:
			soup = BeautifulSoup(espn_nba, 'lxml')
	except urllib.error.HTTPError as e:
		print(e)
	except urllib.error.URLError as u:
		print(u)

	return soup

def final_endpt(soup,target):
	#expand for crawl or user input later (?)
	target = "https://www.espn.com/nba/scoreboard"
	t = BeautifulSoup(urlopen("https://www.espn.com/nba"),'lxml')
	url_components = urllib.parse.urlparse(target)
	individual_path = url_components.path.split('/')
	# we have the url path 
def main():
	""" process flow:
	gather URL -> grab robotx.txt // check if our endpoint url is valid and scrape-able"""
	url = "https://www.espn.com/"
	walkway = "nba/scoreboard/"
	try : 
		robot_text = allow_robot(url+walkway)
	except : 
		print("url path is not allowed")

	try: 
		soup = starting_soup(url+walkway)
	except : 
		print("soup error")

	#robot text has our allow/disallow rules
	#need to grab our end point /nba/scoreboard
	#our static end point for now"
	pathing = "nba/scoreboard/"
	pathing.split("/")


	#soup = starting_soup(url)
	#final_endpt(soup,"")
	#allow_robot(url, "")
	#we can add user input to pick which link they want to follow but for now aiming to get to NBA->Schedule or Scoreboard

main()

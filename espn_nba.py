#extracting matchups for NBA games happening today

from bs4 import BeautifulSoup
from urllib.request import urlopen


decoder_type = "utf-8"


#hard code our url but can be removed to be more flexible as development progresses
def parse_NBA(url = "https://www.espn.com"):
	
	#nav espn for the NBA link
	try:
		nba_page = urlopen(url)
	except urllib.error.HTTPError as e:
		print(e)
	except urllib.error.URLerror as u:
		print(u)

	raw_html = nba_page.read().decode(decoder_type)
	

parse_NBA()

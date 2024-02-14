from urllib.request import urlopen

target_site = "https://www.espn.com" #fill in or user prompt

#check for robots.txt and see if what we're doing is allowed

target_site +=  "robots.txt" if target_site[-1] == "/" else "/robots.txt"

#open url/get html txt to prep parse

page = urlopen(target_site)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

#urllib has built in robot parser

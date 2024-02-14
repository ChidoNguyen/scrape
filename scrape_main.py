#this file contains more finalize code cleaned up from scrape_prac and what not

from urllib.request import urlopen
import  urllib.robotparser

#user input later if we want
#for now messing with espn.com

def robotparser_setup(url):
	user_agent = "*"
	target_site = url
	rule_bot = urllib.robotparser.RobotFileParser() #init our RFP object to handle robot.txt processing
	rule_bot.set_url(target_site +"/robots.txt")
	rule_bot.read()
	return rule_bot

def req_limitations(rule_bot,user_agent):
	#request limitations"
	rLimit = rule_bot.request_rate(user_agent)
	limit_doc = {"requests" : None , "seconds" : None , "crawl_delay" : None}
	try:
		limit_doc["requests"] = rLimit.requests
	except:
		pass
	try:
		limit_doc["seconds"] = rLimit.seconds
	except:
		pass
	try:
		limit_doc["crawl_delay"] = rule_bot.crawl_delay(user_agent) 
	except:
		pass
	return limit_doc

def main():
	u_agent = "*" #generic for everyone unless specified i.e. user_agent = GPTChat
	url = "https://www.espn.com"
	pars_bot = robotparser_setup(url)
	fence = req_limitations(pars_bot,"*")
	#hard coded for now , can add user input later for if fetching is allowed
	if pars_bot.can_fetch(u_agent, "https://www.espn.com/nba"):
		print("do work")
	else:
		print("cannot fetch specified path")
main()

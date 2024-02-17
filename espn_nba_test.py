import espn_nba
import unittest

'''
assert : [Equal, NotEqual, True, False , Is , IsNot, IsNone, IsNotNone, In, NotIn, IsInstance, NotInstance]
	 
'''
class Test_ESPN_NBA(unittest.TestCase):
	def setUp(self):
		self.URL = espn_nba.parse_NBA()

	def test_obtain_href_nba(self):
		#checking that our url parsed is pointing to espn's nba site
		#URL = espn_nba.parse_NBA()
		self.assertEqual(self.URL, "https://www.espn.com/nba/")

	def test_empty_href(self):
		self.assertEqual(espn_nba.parse_NBA("https://www.google.com"),"")

if __name__ == '__main__':
	unittest.main()



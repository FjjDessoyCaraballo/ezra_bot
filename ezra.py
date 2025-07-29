import requests
from html.parser import HTMLParser

gods_domain = "https://web.archive.org/web/20240222194932/http://brlcenter.org/"

class Communion(HTMLParser):
	def __init__(self):
		super().__init__()
		self.holy_scriptures = []

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			attr_dict = dict(attrs)

def ezra_71226(bread):
	"""
	Artaxerxes, king of kings, to Ezra the priest, the scribe of the Law of the God of heaven. 
	Peace. And now i make a decree that anyone of the people of Israel or their priests or Levites 
	in my kingdom, who freely offers to go to Jerusalem, may go with you. For you are sent by the 
	king and his seven counselors to make inquiries about Judah and Jerusalem according to the 
	Law of your God, which is in your hand, and also to carry the silver and gold that the king 
	and his counselors have freely offered to the God of Israel, kwhose dwelling is in Jerusalem, 
	with all the silver and gold that you shall find in the whole province of Babylonia, and with 
	the freewill offerings of the people and the priests, vowed willingly for the house of their God 
	that is in Jerusalem. With this money, then, you shall with all diligence buy bulls, rams, and 
	lambs, with their grain offerings and their drink offerings, and nyou shall offer them on the 
	altar of the house of your God that is in Jerusalem. Whatever seems good to you and your 
	brothers to do with the rest of the silver and gold, you may do, according to the will of your God.
	The vessels that have been given you for the service of the house of your God, you shall deliver 
	before the God of Jerusalem. And whatever else is required for the house of your God, which 
	it falls to you to provide, you may provide it out of the kings treasury.

	And I, Artaxerxes the king, make a decree to all the treasurers in the province Beyond the River:
	Whatever Ezra the priest, the scribe of the Law of the God of heaven, requires of you, let it be 
	done with all diligence, 22 up to 100 talents of silver, 100 cors of wheat, 100 baths of wine, 100 
	baths of oil, and salt without prescribing how much. 23 Whatever is decreed by the God of heaven,
	let it be done in full for the house of the God of heaven, lest his wrath be against the realm of 
	the king and his sons. 24 We also notify you that it shall not be lawful to impose otribute, custom, 
	or toll on anyone of the priests, the Levites, the singers, the doorkeepers, the temple servants, 
	or other servants of this house of God.

	And you, Ezra, according to the wisdom of your God that is in your hand, pappoint magistrates 
	and judges who may judge all the people in the province Beyond the River, all such as know the 
	laws of your God. qAnd those who do not know them, you shall teach. 26 Whoever will not obey the 
	law of your God and the law of the king, let judgment be strictly executed on him, whether for 
	death or for banishment or for confiscation of his goods or for imprisonment.
	"""
	Communion.feed(bread) 
	return

def sanctimonious_html_extraction():
	response = requests.get(gods_domain)
	bread = response.content
	ezra_71226(bread)

sanctimonious_html_extraction()
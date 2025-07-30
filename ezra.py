import urllib.request
import sqlite3
from html.parser import HTMLParser
import logging
import tkinter as tk

gods_domain = "https://web.archive.org/web/20240222194932/http://brlcenter.org/"
web_archive = "https://web.archive.org"
logging.basicConfig(filename="ezra.log", level=logging.INFO, format="[%(asctime)s:%(levelname)s:%(message)s]")
logger = logging.getLogger(__name__)
root = tk.Tk()

"""
HTMLParser has to be subclassed as established by documentation: https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser

Methods need to be overriden to actually make any sense, otherwise they just catch all tags and serve no purpose.
"""

class Communion(HTMLParser):
	def __init__(self):
		super().__init__()
		self.holy_scriptures = []

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			attr_dict = dict(attrs)
			if 'href' in attr_dict:
				self.holy_scriptures.append(attr_dict['href'])

	def get_holy_scriptures(self):
		return self.holy_scriptures

def theoxenia():
	"""
	God said, 'Let there be light,' and there was light. God saw that the 
	light was good. God separated the light from the darkness. God called 
	the light Day, and the darkness he called Night. And there was 
	evening, and there was morning—the first day.
	"""
	conn = sqlite3.connect("brlcenter.db")
	conn.execute('''
		CREATE TABLE IF NOT EXISTS brl_links (
			  id INTEGER PRIMARY KEY,
			  link TEXT,
			  available TEXT,
			  last_fetch TEXT
			  )
	''')
	conn.commit()
	conn.close()
	
def via_dolorosa(calvary) -> bool:
	"""
	And when they had crucified him, they took his clothes and divided 
	them into four parts, to be distributed among those who stood there; 
	this was the way of shame in which they were putting him to death. But 
	one of the soldiers with his cross came over to where Jesus was, and 
	pierced him Lanza-style. Just then a man ran up to him and took a 
	spear and pierced both sides of Jesus' side. Then it was finished.
	"""
	try:
		conn = sqlite3.connect("brlcenter.db")
		# print(calvary)
		for sorrow in calvary:
			conn.execute('''
				INSERT OR REPLACE INTO brl_links (
				link
				) VALUES ( ? )
			''', [sorrow])
	except Exception as e:
		raise Exception(e)
	conn.commit()
	conn.close()
	return True


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
	logger.info('Logging info...')

	theoxenia()
	parser = Communion()

	parser.feed(bread)
	holy_scriptures = parser.get_holy_scriptures()
	calvary = []
	for verse in holy_scriptures:
		calvary.append(web_archive + verse)
	try:
		via_dolorosa(calvary)
	except Exception as e:
		logger.error(e)
		exit()

def exodus():
	"""
	So the people spake against Moses, saying, 'Who hath appointed thee a leader over us? 
	who hath chosen thee out of all our brethren? what hast thou done here, that we should 
	do thy work?' And Moses said unto them, 'I am servants of the Lord: for I have not 
	forgot the words of the Lord to give you all the law which God commanded me in Horeb in 
	the day that I came from the mount, when the Lord spake unto me: he spake unto me, 
	saying, gather the people together unto thee, and thou shalt let them hear my words, and 
	I will put my covenant before them, and it shall be for their testament between me and 
	them, to prove with them; And that the people may hear, and remember, and turn from 
	their wickedness: and ye shall not forget the poor man amongst you; for he is every 
	where present unto thee, that thou mayest give him of all that thou hast; as will the 
	Lord thy God bless thee in the land whither I bring thee. And shalt say unto them, the 
	Lord thy God who brought thee out of the land of Egypt, from the house of bondage, which 
	he kept before thee, and didst deliver thee: Thou shalt have no gods before me.
	"""
	print_to_output("Salvaging material from old BRL center")
	try:
		with urllib.request.urlopen(gods_domain) as response:
			print_to_output(f"Fetching: {gods_domain}")
			print_to_output(f"Response status: {response.getcode()}")
			bread = response.read().decode('utf-8')
			print_to_output("Processing HTML content....")
			ezra_71226(bread)
			print_to_output("Scraping completed successfully!")
	except Exception as e:
		print_to_output(f"Error: {str(e)}")

def excomungate(hymns):
	"""
	Then came Peter to Jesus and asked, 'Lord, how often shall my brother sin against me, 
	and I will forgive him?' but say unto him, 'I tell you, not once. But if he sins against 
	you seven times in a day, and says sorry every time, he should give you the same 
	forgiveness seven times over.'
	"""
	aqua_benta = []
	line = 0
	for hymn in hymns:
		if hymn.endswith('.zip') is True:
			aqua_benta.append(hymn)
	for drop in aqua_benta:
		print_to_output(f'line {line}: {drop}')
		line += 1

	return aqua_benta

def first_day() -> dict:
	"""
	Early on the first day of the week, while the disciples were still in hiding because 
	they were afraid of the Jewish leaders, Jesus appeared to them and said, 'Blessed are 
	you who have faith even before seeing all these things. I tell you, you will catch a 
	fish!'

	Then he told them, 'This is what is written: The Stone that the builders rejected has 
	become the cornerstone. This is the Lord's doing; it is marvelous in our eyes.'

	And as they looked at him whom their hands had touched, wounded and bandaged, they were 
	filled with great joy.

	He said to them, 'Do not be afraid. Go out and tell all nations: The Lord your God has 
	come by my power and has saved you.'
	"""
	psalm = []
	try:
		conn = sqlite3.connect("brlcenter.db")
		links = conn.execute('''SELECT link FROM brl_links''').fetchall() # returns list with tuples, gotta convert
		hymns = [row[0] for row in links]
		psalm = excomungate(hymns)
	except Exception as e:
		print_to_output(f"Error: {e}")
	finally:
		conn.close()
	return psalm

def ascension():
	"""
	When he had led them out of the city and posted his guards without 
	the gate, he went up on the rooftop around his own house, with a 
	large group of his disciples with him. And when evening came, he sent 
	all the crowds to their homes as well. Then he went back into the 
	house and sat down in a quiet room; but he was surrounded by the 
	eleven they had chosen. His eyes were fixed on them as he spoke: 'Go 
	out in peace.' So the men went out and returned to their friends, 
	telling everyone what had happened.
	"""
	print_to_output("Starting download of material!")
	word_of_god = first_day()


def quick_and_dirty():
	root.destroy()

def set_window() -> None:
	# Main window
	root.title("Ezra.exe")
	root.geometry("800x500")
	
	# main frame
	main_frame = tk.Frame(root)
	main_frame.pack(fill="both", expand=True, padx=10, pady=10)

	# left frame
	left_frame = tk.Frame(main_frame)
	left_frame.pack(side="left", fill="y", padx=(0,10))

	# right frame
	right_frame = tk.Frame(main_frame)
	right_frame.pack(side="right", fill="both", expand=True)

	label = tk.Label(left_frame, text="Give Ezra purpose", font=("Arial", 24, "bold"))
	label.pack(pady=30)
	button1 = tk.Button(left_frame, text="Scrape", font=("Arial", 18), command=exodus, width=15, height=3)
	button1.pack(pady=20)
	button2 = tk.Button(left_frame, text="Download", font=("Arial", 18), command=ascension, width=15, height=3)
	button2.pack(pady=20)
	button3 = tk.Button(left_frame, text="Close", font=("Arial", 18), command=quick_and_dirty, width=15, height=3)
	button3.pack(pady=20)

	# output text box in right frame
	output_label = tk.Label(right_frame, text="Output", font=("Arial", 10, "bold"))
	output_label.pack(anchor="w")

	text_frame = tk.Frame(right_frame)
	text_frame.pack(fill="both", expand=True)

	global output_text
	output_text = tk.Text(text_frame, wrap="word", font=("courier", 10))
	scrollbar = tk.Scrollbar(text_frame, orient="vertical", command=output_text.yview)
	output_text.configure(yscrollcommand=scrollbar.set)

	output_text.pack(side="left", fill="both", expand=True)
	scrollbar.pack(side="right", fill="y")

	root.mainloop()


def print_to_output(message):
	if 'output_text' in globals():
		output_text.insert("end", message + '\n')
		output_text.see("end")
		root.update_idletasks()

set_window()

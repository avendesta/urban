# This function will scrap meaning of a word from Urban dictionary website

from bs4 import BeautifulSoup
import requests

def urban(word):
	source = requests.get(f'https://www.urbandictionary.com/define.php?term={word}').text
	source = source.replace("\\r","\n\n")
	source = source.replace("\r","\n")

	soup = BeautifulSoup(source,'lxml')

	found = soup.findAll('div',class_='def-panel')
	res = []
	for f in found:
		word = f.find('div',class_='def-header').a.text
		meaning = f.find('div',class_='meaning').text
		example  = f.find('div',class_='example').text
		# example = example.encode('unicode-escape').decode().replace('\\\\', '\\')
		res.append( {'word':word, 'meaning':meaning, 'example':example} )

	return res

print(urban("Covid")[5])
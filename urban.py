# This function will scrap meaning of a word from Urban dictionary website

from bs4 import BeautifulSoup
import requests

def urban(word):
	source = requests.get(f'https://www.urbandictionary.com/define.php?term={word}').text

	soup = BeautifulSoup(source,'lxml')

	top = soup.find('div',class_='def-panel')

	word = top.find('div',class_='def-header').a.text
	meaning = top.find('div',class_='meaning').text
	example  = top.find('div',class_='example').text
	example = example.encode('unicode-escape').decode().replace('\\\\', '\\')
	return {'word':word, 'meaning':meaning, 'example':example}


print(urban("Donald"))
import requests  # importing requests to make HTTP request
from bs4 import BeautifulSoup  # importing it to work with html tags

print('Type "en" if you want to translate from French into English, or "fr" if you '
      'want to translate from English into French:')

headers = {'User-Agent': 'Mozilla/5.0'}  # Presenting itself as browser

language_selected = input()  # taking target language from user

from_language = ''
to_language = ''
if language_selected == 'fr':
      from_language = 'french'
      to_language = 'english'

elif language_selected == 'en':
      from_language = 'english'
      to_language = 'french'


print('Type the word you want to translate:')

word_to_translate = input()  # taking word to translate

print(f'You chose {language_selected} as a language to translate {word_to_translate}.')

# making url dynamically by taking user input as arguments to make complete url

url = f'https://context.reverso.net/translation/{from_language}-{to_language}/{word_to_translate}'

# sending HTTP request as get method with target url and header details
page = requests.get(url, headers=headers)









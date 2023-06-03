import requests  # importing requests to make HTTP request
from bs4 import BeautifulSoup  # importing it to work with html tags

print('Type "en" if you want to translate from French into English, or "fr" if you '
      'want to translate from English into French:')

headers = {'User-Agent': 'Mozilla/5.0'}  # Presenting itself as browser

language_selected = input()  # taking target language from user

# selecting language to translate from language to translate too
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

print(page.status_code, 'OK')

soup = BeautifulSoup(page.content, 'html.parser')

# translated words
words = soup.find_all('span', {'class': 'display-term'})
# translated words examples
examples = soup.find_all('div', {'class': 'example'})

translations_of_word = []

examples_of_sentences = []

# print('Translations')
#
# for word in words:
#    translations_of_word.append(word.text)
#
# for example in examples:
#     examples_of_sentences.append(example.text.strip().replace('\n', '').replace('\r', ''))
#
# print(translations_of_word)
# print(examples_of_sentences)

print('Translations')

for word in words:
    translations_of_word.append(word.text.strip())

for example in examples:
    source, target = example.find_all('span', {'class': 'text'})
    source_text = source.text.strip().replace('\n', '').replace('\r', '')
    target_text = target.text.strip().replace('\n', '').replace('\r', '')
    examples_of_sentences = examples_of_sentences + [source_text, target_text]

# for index, (source_text, target_text) in enumerate(examples_of_sentences):
#     print(f'{index+1}. {source_text}')
#     print(f'   {target_text}')
print(translations_of_word)
print(examples_of_sentences)
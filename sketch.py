from json import load, dump
from time import sleep
from random import choice
from scraping import Page
import codecs
# load data file
with open('words.json', 'r') as datafile:
    data = load(datafile)
# test if there are all the stuff there even
def test_word_defs(page:Page):
    list_of_def = []
    # css-1avshm7 e16867sm0 is the class of the definition div
    def_div = page.soup.find('div', attrs={'class':'css-1avshm7 e16867sm0'})
    normal_def = def_div.find('p', attrs={'class':'e1w1pzze4'})
    if normal_def:
        return [{'pos':None, 'defs':[normal_def.text]}]
    # css-109x55k e1hk9ate4 is the calss for definition sections for every PoS
    def_div_sections = def_div.find_all('section', attrs={'class': 'css-109x55k'})
    # css-69s207 e1hk9ate3 is the class for PoS
    for section in def_div_sections:
        pos = section.find('div', attrs={'class':'css-69s207 e1hk9ate3'})
        pos_test = pos.find('div', attrs={'class':'luna-pos'})
        if pos_test:
            pos = pos_test.text
        elif pos:
            pos = pos.text
        else:
            pos = None
        # css-10n3ydx e1hk9ate0 is the class of def
        defs_parent = section.find('div', attrs={'class':'css-10n3ydx e1hk9ate0'})
        defs = [i.text for i in defs_parent.find_all('div', attrs={'class':'e1q3nk1v2'})]
        list_of_def.append({'pos':pos, 'defs':defs})
    return list_of_def
# use data
if __name__ == "__main__":
    # DATA = ["https://www.dictionary.com/browse/zebulon",
    # "https://www.dictionary.com/browse/concrete",
    # "https://www.dictionary.com/browse/cost",
    # "https://www.dictionary.com/browse/exaggerated",
    # "https://www.dictionary.com/browse/amount",
    # "https://www.dictionary.com/browse/neonatal",
    # "https://www.dictionary.com/browse/aggrandisement",
    # "https://www.dictionary.com/browse/zebulon",
    # "https://www.dictionary.com/browse/delivery",
    # "https://www.dictionary.com/browse/count",
    # "https://www.dictionary.com/browse/in-loco-parentis",
    # "https://www.dictionary.com/browse/directress",
    # "https://www.dictionary.com/browse/palampore",
    # "https://www.dictionary.com/browse/interdependability",
    # "https://www.dictionary.com/browse/tracker-fund",
    # "https://www.dictionary.com/browse/placental-membrane",
    # "https://www.dictionary.com/browse/pou-sto",
    # "https://www.dictionary.com/browse/antisecretory",
    # "https://www.dictionary.com/browse/gieseking",
    # "https://www.dictionary.com/browse/fructosan",
    # "https://www.dictionary.com/browse/keen"]
    words = []
    x = 0
    for word in data:
        try:
            definition = test_word_defs(Page(word['link']))
            new_word = { 'word':word['word'], 'results': definition}
            # word['results'] = definition
            words.append(new_word)
            print(new_word)
            if x % 5000:
                with open(f"{x}.json", 'w+') as datafile:
                    dump(words, datafile)
                    words = []
        except Exception:
            with codecs.open('log.txt','a+', 'utf-8') as log:
                log.write(f"{x}\t{word['link']}\n")
        x += 1
from json import load, dump
# from time import sleep
# from random import choice
from scraping import Page
from mail import mail_it


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
    mail_it({'Starting':'Operations'}, 69)
    print("""
    ==============================
    ==============================
        STARTING WEB SCRAPING
    ==============================
    ==============================
    """)
    words = []
    errors = []
    x = 0
    # print(data.__len__())
    # just ot check if heroku can actually allow file system mods 

    for word in data:
        x += 1
        try:
            definition = test_word_defs(Page(word['link']))
            new_word = {'word':word['word'],'results': definition}
            # word['results'] = definition
            words.append(new_word)
            # print(new_word)
            print(new_word)
            if x % 50000 == 0:
                mail_it(word, x)
                words = []
            if x % 1000 == 0:
                Page("https://cloud-computer.herokuapp.com")
        except Exception:
            errors.append({'word':word['word'],'link':word['link'],'id':str(x)})
    mail_it(words, x)
    mail_it(errors, 0)
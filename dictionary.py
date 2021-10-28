from json import load, dump
# from difflib import get_close_matches

data = load(open('dictionary.json'))

word = "Cheese"

while word:
    print('\n')
    word = input("Please Enter your query word: ")
    print('\n')
    if word:
        for i in data:
            if i['word'].lower() == word.lower():
                x = 1
                for j in i['results']:
                    print(f"{x}\t{j['pos']}")
                    x += 1
                    y = 1
                    print('\n')
                    for k in j['defs']:
                        print(f"\t{y}\t{k}")
                        y += 1
                    print('\n')

        




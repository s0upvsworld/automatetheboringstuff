import re
atRegex = re.compile(r'.at')
matches = atRegex.findall('That cat in the hat sat on the flat mat.')

search_word = input('Search word:\n')
for search_word in matches:
    print(search_word)

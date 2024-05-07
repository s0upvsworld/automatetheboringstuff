import re

phoneNumbRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumbRegex.findall('Call me 401-423-1153 tomorrow, or at 401-423-2091'))

TestWordRegex = re.compile(r'Red Sox: Win')
print(TestWordRegex.findall('Rays: Win, Dodgers: Lose, Red Sox: Win'))
import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex.search('My phone number is 401-423-1153. Call me tomorrow')
mo.group()
print(mo.group())

phoneRegex.search('My phone number is 423-1153. Call me tomorrow')
mo == None

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d')
phoneRegex.search('My phone number is 423-1153. Call me tomorrow')
phoneRegex.search('My phone number is 423-1153. Call me tomorrow')



batRegex = re.compile(r'Bat(wo)*man')
batRegex = re.compile(r'Bat(wo)+man')

haRegex = re.compile(r'(Ha){3}')
haRegex.Search('He said "Hahaha"')


phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
phoneRegex.search('My phone numbers are 401-423-1153, 423-2091, and 401-423-1876')


"""





"""
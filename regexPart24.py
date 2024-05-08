import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 401-423-1153')

mo = phoneNumRegex.search('My number is 401-423-1153')
print(mo.group())
mo.group()

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 401-423-1153')
print(mo.group(1))


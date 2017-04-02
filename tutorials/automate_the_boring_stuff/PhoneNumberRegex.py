import re
phoneNumRegex = re.compile(r'(\d\d\d-)?(\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo1.group())
mo2 = phoneNumRegex.search('My number is 555-4242.')
print('Phone number found: ' + mo2.group())
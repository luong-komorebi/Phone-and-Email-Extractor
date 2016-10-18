# phoneAndEmail.py - Finds phone numbers and email adresses on the clipboard

import pyperclip, re

# Create PhoneRegex object and EmailRegex Object
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
  )''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
  )''', re.VERBOSE)

# Copy the input from the clipboard and use it to search
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Paste input back to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('All copied to Clipboard : ')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails was found! ')

""" Copy these to clipboard to test:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
"""
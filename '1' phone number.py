# !python3

import re, pyperclip
# Regex for phone number
num = re.compile(r'''
    # +91 OPTIONAL
((\d\d)?
    #11,9,8
(\d\d\d\d\d\d\d\d\d\d\d|\d\d\d\d\d\d\d\d\d|\d\d\d\d\d\d\d\d\d))        
''',re.VERBOSE)
# Regex for email
email = re.compile('''
#email
    #name
[a-zA-z0-9_.+]+    
    #@
@
    #domine
[a-zA-z0-9_.+]+  
    #extension
''',re.VERBOSE)
# get text from clipboad
text= pyperclip.paste()
# extract email and phone number from text
extp = num.findall(text)
exte= email.findall(text)

apn = []
for pn in extp:
    apn.append(pn[0])

print(str(apn))
# copy all to clipboad
result = '\n'.join(apn)+ '\n'.join(exte)
pyperclip.copy(result)

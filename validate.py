import re
email = input('what is your email?').strip()

'''username, domain = email.split('@')

#if (username) and ('.' in domain):
if username and domain.endswith('.edu'):
    print ('valid')
else: 
    print('invalid')'''


# a dot = any character, * = 0 or more repetitions, + = 1 or more repetitions
if re.search(r'^(\w|\.)+@(\w+\.)?\w+\.(com|edu|org|uk)$', email, re.IGNORECASE): 
    print('valid')
else :
    print('invalid')
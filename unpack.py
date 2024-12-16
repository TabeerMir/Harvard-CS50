'''
def total(galleons, sickles, knuts):
    return (galleons*17+sickles)*29+knuts

coins = [100,50,25]

print(total(*coins), ' knuts')
'''


def f(*args,**kwargs):
    print('named:', kwargs)#print('positional:', args)

#f(100,50,25)
f(galleons=100, sickles =50, knuts = 25)




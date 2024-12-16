'''
import random #by importing random all its contents are scoped to the random module and you can have your own chocie function or variable without colliding

coin = random.choice(['heads', 'tails']) #choice iterates over a list
print(coin)

'''

from random import choice 
coin = choice(['heads', 'tails'])

import random
number = random.randint(1,10)
print(number)

cards =['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards :
    print(card)
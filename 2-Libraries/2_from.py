#From keyword is used to import some specific functions/parts from a specific module
from random import choice,randint,shuffle #now we dont need to specify random.choice everywhere

s = choice(["Nabin" , "Nitin"])
#print(s)
#Letsee some more functions in the random module like randint(a,b) a and b are inclusive
number = randint(1,10)
#print(number)
#shuffle - shuffles values
cards = ["queen", "jack" , "king"]
shuffle(cards)
for card in cards :
    print(card)


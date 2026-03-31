import random

# coin_toss = random.choice(["heads", "tail"])
# print(coin_toss)

# from random import choice
# coin_toss = choice(["heads", "tail"])
# print(coin_toss)

# rand_int = random.randint(1, 10)
# print(rand_int)

cards = ["Queen" , "King" , "Jack" , "Ace"]
random.shuffle(cards)

for card in cards:
   print(card)

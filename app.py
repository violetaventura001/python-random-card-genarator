import random

card_suite = ["♡","♧","♤","♢"]
card_numbers =["2","3","4","5","6","7","8","9","10","A","K","Q","J"]

def get_random_card(a):
    return random.randint(0,len(a)-1)

print(card_numbers[get_random_card(card_numbers)] +" "+ card_suite[get_random_card(card_suite)])
#print(card_suite[get_random_card(card_suite)])

#print(card_suite[-1])
#+""+card_suite[get_random_card()]
import random

card_suite = [" ♡ ", " ♧ ", "♤", "♢"]
card_numbers =["1","2","3","4","5","6","7","8","9","10","A","K","Q","J"]

def get_random_card():
    return random.randint(0,13)

print(card_numbers[get_random_card()])

#+""+card_suite[get_random_card()]
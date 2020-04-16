import random

card_suite = [" ♡ ", " ♧ ", "♤", "♢"]
card_numbers =["1","2","3","4","5","6","7","8","9","10","A","K","Q","J"]

def get_random_card():
    return random.randint(0,13)

print(card_suite[3]+""+card_numbers[4])
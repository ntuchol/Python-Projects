import random

def coin_toss():
    result = random.choice(['Heads', 'Tails'])
    return result

for i in range(10):
    print(f"Toss {i+1}: {coin_toss()}")

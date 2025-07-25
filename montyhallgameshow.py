import random

def monty_game(chances, switch_strategy=True):
    
    global goatcount
    global carcount
    
    carcount = 0
    goatcount = 0

    for i in range(chances):
        doors = [0, 0, 0]
        car_door = random.randint(0,2)
        doors[car_door] = 1
        
        first_choice = random.randint(0,2)
        

        monty_choice = [x for x in range(3) if x != first_choice and doors[x]==0]
        
        second_choice = random.choice(monty_choice)
        
        if switch_strategy:
            third_choice = next(x for x in range(3) if x != first_choice and x != second_choice)
        
            if doors[third_choice] == 1:
                carcount += 1
            else:
                goatcount +=1
        
    wining_percentage = (carcount/chances)*100
    return wining_percentage

chances = 1000

switch_win_percentage = monty_game(chances, switch_strategy=True)

print(f" I won {carcount} times ")
print(f" Win percentage with switching: {switch_win_percentage:.2f}%")

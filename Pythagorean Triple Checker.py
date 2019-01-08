#Pythagorean Triple Checker 
sides = []
a = int(input('Please input a side length of the triangle:'))
b = int(input('Please input another side length:'))
c = int(input('Please input the last side length:'))
sides += [a,b,c] # add the 3 inputs to the list of sides
sides = sorted(sides) # sorting the sides

if sides[0]**2+sides[1]**2 == sides[2]**2 :
    print('It is a pythagorean triple')
else:
    print('It is not a pythagorean triple')

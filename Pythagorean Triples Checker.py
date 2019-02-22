triangle["side1"]= int(input("enter a value for side 1 or 0 to quit:"))
if triangle["side1"] == 0:
	break
else:
	triangle["side2"]= int(input("enter a value for side2:"))
	triangle["side3"]= int(input("enter a value for side 3:"))
	if triangle["side2"]< triangle["side1"] > triangle ["side3"]:
		 c = triangle ["side1"]
		 b = triangle ["side2"]
		 a = triangle ["side3"]
	elif triangle["side1"] < triangle["side2"] > triangle["side3"]:
		 c = triangle ["side2"]
		 b = triangle ["side1"]
		 a = triangle ["side3"]
	else:
		c = triangle["side3"]
		b = triangle["side2"]
		a = triangle["side1"]
if a**2 + b**2 == c**2:
	print("You have a pythagorean triple")
else:
	print("You do not have a pythagorean triple")

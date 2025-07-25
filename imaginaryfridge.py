my_fridge = {} 

my_fridge["apples"] = 5
my_fridge["milk"] = 2
my_fridge["cheese"] = 1

if "apples" in my_fridge:
  print(f"We have {my_fridge['apples']} apples.")
else:
  print("We don't have any apples.")

if "grapes" in my_fridge:
  print(f"We have {my_fridge['grapes']} grapes.")
else:
  print("We don't have any grapes.")

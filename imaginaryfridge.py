my_fridge = {}  # Create an empty dictionary for the fridge

# Add some food items
my_fridge["apples"] = 5
my_fridge["milk"] = 2
my_fridge["cheese"] = 1

# Check if we have apples
if "apples" in my_fridge:
  print(f"We have {my_fridge['apples']} apples.")
else:
  print("We don't have any apples.")

# Check if we have grapes
if "grapes" in my_fridge:
  print(f"We have {my_fridge['grapes']} grapes.")
else:
  print("We don't have any grapes.")
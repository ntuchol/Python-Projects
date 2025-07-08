def calculate_stamps(weight, stamp_weight_limit):
    # Calculate the number of stamps needed
    stamps = (weight + stamp_weight_limit - 1) // stamp_weight_limit  # Ceiling division
    return stamps

# Example usage
weight = 120  # Weight of the mail in grams
stamp_weight_limit = 50  # Each stamp covers 50 grams
stamps_needed = calculate_stamps(weight, stamp_weight_limit)
print(f"You need {stamps_needed} stamps.")

def calculate_stamps_cost(postage_cost, stamp_value):
    # Calculate the number of stamps needed
    stamps = (postage_cost + stamp_value - 1) // stamp_value  # Ceiling division
    return stamps

# Example usage
postage_cost = 2.75  # Total postage cost in dollars
stamp_value = 0.55  # Value of one stamp in dollars
stamps_needed = calculate_stamps_cost(postage_cost, stamp_value)
print(f"You need {stamps_needed} stamps.")

def calculate_stamps(weight, stamp_weight_limit, stamp_value, cost_per_gram):
    # Calculate total postage cost based on weight
    total_cost = weight * cost_per_gram
    # Calculate the number of stamps needed
    stamps = (total_cost + stamp_value - 1) // stamp_value  # Ceiling division
    return stamps

# Example usage
weight = 120  # Weight in grams
stamp_weight_limit = 50  # Each stamp covers 50 grams
stamp_value = 0.55  # Value of one stamp in dollars
cost_per_gram = 0.02  # Cost per gram in dollars
stamps_needed = calculate_stamps(weight, stamp_weight_limit, stamp_value, cost_per_gram)
print(f"You need {stamps_needed} stamps.")


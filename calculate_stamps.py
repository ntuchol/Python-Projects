def calculate_stamps(weight, stamp_weight_limit):
    stamps = (weight + stamp_weight_limit - 1) // stamp_weight_limit 
    return stamps

weight = 120  
stamp_weight_limit = 50  
stamps_needed = calculate_stamps(weight, stamp_weight_limit)
print(f"You need {stamps_needed} stamps.")

def calculate_stamps_cost(postage_cost, stamp_value):
    stamps = (postage_cost + stamp_value - 1) // stamp_value  # Ceiling division
    return stamps

postage_cost = 2.75  
stamp_value = 0.55  
stamps_needed = calculate_stamps_cost(postage_cost, stamp_value)
print(f"You need {stamps_needed} stamps.")

def calculate_stamps(weight, stamp_weight_limit, stamp_value, cost_per_gram):
    total_cost = weight * cost_per_gram
    stamps = (total_cost + stamp_value - 1) // stamp_value  # Ceiling division
    return stamps

weight = 120  
stamp_weight_limit = 50 
stamp_value = 0.55 
cost_per_gram = 0.02 
stamps_needed = calculate_stamps(weight, stamp_weight_limit, stamp_value, cost_per_gram)
print(f"You need {stamps_needed} stamps.")


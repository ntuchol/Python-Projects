def calculate_municipal_bond_interest(face_value, annual_interest_rate, years):
    
    rate_decimal = annual_interest_rate / 100
    total_interest = face_value * rate_decimal * years
    return total_interest

face_value = 10000  
annual_interest_rate = 4.5  
years = 10  
interest_earned = calculate_municipal_bond_interest(face_value, annual_interest_rate, years)
print(f"Total interest earned on the municipal bond: ${interest_earned:,.2f}")


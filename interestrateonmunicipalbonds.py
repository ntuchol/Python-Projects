# Function to calculate interest on a municipal bond
def calculate_municipal_bond_interest(face_value, annual_interest_rate, years):
    """
    Calculate the total interest earned on a municipal bond.

    :param face_value: The bond's face value (principal amount)
    :param annual_interest_rate: Annual interest rate (as a percentage, e.g., 5 for 5%)
    :param years: Number of years the bond is held
    :return: Total interest earned
    """
    # Convert interest rate from percentage to decimal
    rate_decimal = annual_interest_rate / 100
    # Calculate total interest
    total_interest = face_value * rate_decimal * years
    return total_interest

# Example usage
face_value = 10000  # Bond face value in dollars
annual_interest_rate = 4.5  # Annual interest rate in percentage
years = 10  # Number of years held

interest_earned = calculate_municipal_bond_interest(face_value, annual_interest_rate, years)
print(f"Total interest earned on the municipal bond: ${interest_earned:,.2f}")

This is a straightforward way to calculate interest, but you can expand it to include compounding or tax considerations if needed! Let me know if you'd like to explore those. 😊
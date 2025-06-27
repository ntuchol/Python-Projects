def calculate_future_value(present_value, annual_rate, years):
    """
    Calculate the future value of an investment.

    :param present_value: Initial investment amount (float)
    :param annual_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%)
    :param years: Number of years the money is invested (int or float)
    :return: Future value of the investment (float)
    """
    future_value = present_value * (1 + annual_rate) ** years
    return future_value

# Example usage
present_value = 1000  # Initial investment in dollars
annual_rate = 0.05    # 5% annual interest rate
years = 10            # Investment period in years

future_value = calculate_future_value(present_value, annual_rate, years)
print(f"The future value of the investment is: ${future_value:.2f}")
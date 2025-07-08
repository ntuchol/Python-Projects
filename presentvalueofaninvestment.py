def calculate_present_value(future_value, discount_rate, periods):
    """
    Calculate the present value of an investment.

    :param future_value: The future value of the investment (FV)
    :param discount_rate: The annual discount rate (r) as a decimal
    :param periods: The number of periods (n)
    :return: Present Value (PV)
    """
    present_value = future_value / ((1 + discount_rate) ** periods)
    return present_value

# Example usage
future_value = 10000  # Future value in dollars
discount_rate = 0.05  # 5% annual discount rate
periods = 10          # Investment duration in years

pv = calculate_present_value(future_value, discount_rate, periods)
print(f"The present value of the investment is: ${pv:.2f}")
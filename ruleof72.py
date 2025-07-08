def rule_of_72(interest_rate):
    """
    Calculate the number of years it takes for an investment to double
    using the Rule of 72.

    :param interest_rate: Annual interest rate as a percentage (e.g., 6 for 6%)
    :return: Approximate number of years to double the investment
    """
    if interest_rate <= 0:
        return "Interest rate must be greater than 0."
    return 72 / interest_rate

# Example usage
rate = 6  # Annual interest rate in percentage
years = rule_of_72(rate)
print(f"At an interest rate of {rate}%, it will take approximately {years:.2f} years to double your investment.")
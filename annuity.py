def present_value_annuity(payment, interest_rate, periods):
    """
    Calculate the present value of an annuity.

    :param payment: Payment per period
    :param interest_rate: Interest rate per period (as a decimal)
    :param periods: Number of periods
    :return: Present value of the annuity
    """
    if interest_rate == 0:  # Handle the case where interest rate is 0
        return payment * periods
    return payment * (1 - (1 + interest_rate) ** -periods) / interest_rate

# Example usage
payment = 1000  # Payment per period
interest_rate = 0.05  # 5% interest rate per period
periods = 10  # Number of periods

pv = present_value_annuity(payment, interest_rate, periods)
print(f"The present value of the annuity is: ${pv:.2f}")
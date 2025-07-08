def calculate_ytm(face_value, price, coupon_rate, years_to_maturity):
    """
    Approximate Yield to Maturity (YTM) for a bond.
    """
    annual_coupon = face_value * coupon_rate
    ytm = (annual_coupon + (face_value - price) / years_to_maturity) / ((face_value + price) / 2)
    return ytm

# Example usage
face_value = 1000  # Bond's face value
price = 950        # Current price of the bond
coupon_rate = 0.05 # Annual coupon rate (5%)
years_to_maturity = 10

ytm = calculate_ytm(face_value, price, coupon_rate, years_to_maturity)
print(f"Approximate YTM: {ytm:.2%}")
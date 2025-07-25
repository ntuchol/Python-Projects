def calculate_ytm(face_value, price, coupon_rate, years_to_maturity):
    annual_coupon = face_value * coupon_rate
    ytm = (annual_coupon + (face_value - price) / years_to_maturity) / ((face_value + price) / 2)
    return ytm

face_value = 1000  
price = 950        
coupon_rate = 0.05 
years_to_maturity = 10

ytm = calculate_ytm(face_value, price, coupon_rate, years_to_maturity)
print(f"Approximate YTM: {ytm:.2%}")

def int_to_base_string(number, base):
    
    if not (2 <= base <= 36):  
        raise ValueError("Base must be between 2 and 36.")

    if number == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    is_negative = False

    if number < 0:
        is_negative = True
        number = abs(number)

    while number > 0:
        remainder = number % base
        result.append(digits[remainder])
        number //= base  

    if is_negative:
        result.append("-")

    return "".join(result[::-1]) 

import roman

# Integer to Roman
num = 947
roman_num = roman.toRoman(num)
print(f"{num} in Roman numerals is: {roman_num}")

# Roman to integer
roman_num = 'CMXLVII'
num = roman.fromRoman(roman_num)
print(f"{roman_num} in integer is: {num}")

def int_to_roman(num):
    roman_map = { 1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
    integers = list(roman_map)
    symbols = list(roman_map.values())

    i = 12
    result = ""

    while num != 0:
        if integers[i] <= num:
            result += symbols[i]
            num -= integers[i]
        else:
            i -= 1
    return result

number = 1994
print(f"{number} in Roman numerals is: {int_to_roman(number)}")
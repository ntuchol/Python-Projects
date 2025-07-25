 integer_num = 10
    float_num = 20.5
    string_num1 = str(integer_num)  
    string_num2 = str(float_num) 
    
currency_string = "$1,234.56"
    number_string = currency_string.replace("$", "").replace(",", "")
    amount = float(number_string)  
    
from num2words import num2words
    number = 1234
    words = num2words(number) 

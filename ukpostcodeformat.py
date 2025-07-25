import re

def validate_uk_postcode(postcode):
    pattern = r"^([A-Z]{1,2}\d{1,2}[A-Z]?)\s(\d[A-Z]{2})$"  
    match = re.match(pattern, postcode.upper())
    return bool(match)

print(validate_uk_postcode("SW1A 1AA"))  
print(validate_uk_postcode("L1 8JQ"))   
print(validate_uk_postcode("AA99 9AA")) 
print(validate_uk_postcode("A9 9AA"))  
print(validate_uk_postcode("A9A 9AA"))
print(validate_uk_postcode("AA1 1AA")) 
print(validate_uk_postcode("AA9 9AA")) 

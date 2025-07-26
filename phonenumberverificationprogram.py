import phonenumbers
from phonenumbers import carrier, geocoder, NumberParseException

def verify_phone_number(phone_number, region="US"):
    try:
        parsed_number = phonenumbers.parse(phone_number, region)
        
        if phonenumbers.is_valid_number(parsed_number):
            carrier_name = carrier.name_for_number(parsed_number, "en")
            location = geocoder.description_for_number(parsed_number, "en")
            
            return {
                "valid": True,
                "formatted_number": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "carrier": carrier_name,
                "location": location
            }
        else:
            return {"valid": False, "error": "Invalid phone number"}
    except NumberParseException as e:
        return {"valid": False, "error": str(e)}

if __name__ == "__main__":
    phone_number = input("Enter a phone number (e.g., +1234567890): ")
    result = verify_phone_number(phone_number)
    
    if result["valid"]:
        print("Phone Number is Valid!")
        print(f"Formatted Number: {result['formatted_number']}")
        print(f"Carrier: {result['carrier']}")
        print(f"Location: {result['location']}")
    else:
        print(f"Invalid Phone Number: {result['error']}")

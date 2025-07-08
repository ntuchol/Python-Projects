from datetime import datetime

date_string = "2025-06-07 10:30:00"
format_string = "%Y-%m-%d %H:%M:%S"

datetime_object = datetime.strptime(date_string, format_string)
print(datetime_object)  # Output: 2025-06-07 10:30:00
print(type(datetime_object)) # Output: <class 'datetime.datetime'>
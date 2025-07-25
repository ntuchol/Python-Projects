class OopsException(Exception):
    
    def __init__(self, message="Oops! Something went wrong."):
        self.message = message
        super().__init__(self.message)

try:
    raise OopsException("A specific oops occurred!")
except OopsException as e:
    print(f"Caught an OopsException: {e}")

try:
    result = 10 / 0
except ZeroDivisionError:
    raise OopsException("Division by zero attempted")
except OopsException as e:
    print(f"Caught an OopsException: {e}")

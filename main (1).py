class OopsException(Exception):
    """
    Custom exception class for 'Oops' situations.
    """
    def __init__(self, message="Oops! Something went wrong."):
        self.message = message
        super().__init__(self.message)

# Example of raising and handling the custom exception
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
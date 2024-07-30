
class DivisionByZeroError(Exception):
    def __init__(self, message="Division by zero error: divisor cannot be zero"):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    if b == 0:
        raise DivisionByZeroError()
    return a / b

try:
    result = divide(10, 0)
    print("Result:", result)
except DivisionByZeroError as e:
    print("Exception occurred:", e)

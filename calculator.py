def multiply(a: int, b: int) -> int:
    """Multiply a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b

def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b

def divide(a: int, b: int) -> float:
    """Divide a and b.

    Args:
        a: first int
        b: second int
    """
    return a / b

def subtract(a: int, b: int) -> int:
    """Subtract a and b.

    Args:
        a: first int
        b: second int
    """
    return a - b

def calculator(a: int, b: int, operation: str) -> int:
    """Simple calculator function.

    Args:
        a: first int
        b: second int
        operation: operation to perform
    """
    if operation == "add":
        return add(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        try:
            return divide(a, b)
        except ZeroDivisionError:
            raise ValueError("Cannot divide by zero")
    elif operation == "subtract":
        return subtract(a, b)
    else:
        raise ValueError("Invalid operation provided")
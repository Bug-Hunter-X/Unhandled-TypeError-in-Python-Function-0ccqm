def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
except TypeError:
    return "Invalid input types"

# Example usage that might lead to unexpected behavior:
# This will lead to an unhandled TypeError
print(function_with_uncommon_error(10, '2'))
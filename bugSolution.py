def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid input types. Both inputs must be numbers.")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

# Example usage:
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, '2'))
print(function_with_uncommon_error(10,0))
print(function_with_uncommon_error('abc',10))
def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0  # Or raise a more informative error

result = function(10, 0)
print(result)
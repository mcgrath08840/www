def divide_secure(number, divisor):
    assert divisor != 0, "Divided by zero!"
    # Assertions can be turned off in high performance mode.
    return number / divisor

# Assertions to check for errors you may want to turn off later for performance.

print(divide_secure(10, 0))
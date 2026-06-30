
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)
except ValueError:
    print("Error: You must enter a valid number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

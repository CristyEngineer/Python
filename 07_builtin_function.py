import math

print("Square Root Calculator 🧮")

try:
    number = float(input("Enter a number to find its square root: "))
    
    if number < 0:
        print("Cannot calculate the square root of a negative number.")
    else:
        print(f"The square root of {number} is {math.sqrt(number)}")

except ValueError:
    print("Invalid input. Please enter a valid number.")

print("This program checks whether a number is even or odd.")
try:
    x = int(input("Please enter a number: "))
    is_even = (x % 2 == 0)

    if is_even:
        print("The number is even.")
    else:
        print("The number is odd.")

except ValueError:
    print("Invalid input. Please enter an integer number.")


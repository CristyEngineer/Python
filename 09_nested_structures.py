print("Even or Odd Checker 🔍")

try:
    start = int(input("Enter the starting number (integer): "))
    end = int(input("Enter the ending number (integer): "))

    print(f"\nChecking numbers from {start} to {end}:\n")

    for i in range(start, end + 1):
        if i % 2 == 0:  # nested conditional
            print(i, "is even")
        else:
            print(i, "is odd")

except ValueError:
    print("Invalid input. Please enter whole numbers (integers) only.")

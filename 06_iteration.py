print("Welcome to the Countdown Program! 🚀")

try:
    user_input = input("Enter a starting number (integer): ")
    x = float(user_input)

    if not x.is_integer(): 
        print("Invalid input. Please enter a whole number.")
    else:
        x = int(x)
        print(f"Countdown from {x}:")
        for i in range(x, 0, -1):
            print(i)
        print("🚀!")

except ValueError:
    print("Invalid input. Please enter a valid number.")

try:
    experience = int(input("How many years of work experience do you have? "))

    if experience < 0:
        print("Invalid input.")
    elif experience <= 2:
        print("You are a junior.")
    elif experience <= 5:
        print("You are a mid-level professional.")
    else:
        print("You are a senior.")

except ValueError:
    print("Invalid input. Please enter a number.")

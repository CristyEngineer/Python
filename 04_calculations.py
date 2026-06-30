print("Please enter two numbers and use a dot (.) as the decimal separator.")
try: 
  a = float(input("Number A: ")) 
  b = float(input("Number B: ")) 
  print("The sum of A and B is:", a + b) 
  print("The difference between A and B is:", a - b) 
  print("The product of A and B is:", a * b) 
  if b != 0: 
    print("Division:", a / b) 
  else: 
    print("Division: Cannot divide by zero") 
except ValueError: 
  print("Invalid input. Please enter a number.")

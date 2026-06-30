"""
Interactive shopping list program demonstrating Python list operations.
"""

shopping_list = []

while True:
    print("\nChoose an option:")
    print("1. View list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Sort list")
    print("5. Check item")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("\nShopping list:")
        for item in shopping_list:
            print("-", item)
        if not shopping_list:
            print("(The list is empty)")

    elif choice == "2":
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(f"{item} added.")

    elif choice == "3":
        item = input("Enter an item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed.")
        else:
            print("Item not found.")

    elif choice == "4":
        shopping_list.sort()
        print("List sorted alphabetically.")

    elif choice == "5":
        item = input("Enter an item to check: ")
        if item in shopping_list:
            print(f"{item} is in the list.")
        else:
            print(f"{item} is not in the list.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

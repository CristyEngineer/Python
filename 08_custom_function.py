from datetime import datetime

def greet_user(name):
    """Greet the user based on the time of day and compare hobbies."""
    current_hour = datetime.now().hour
    
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(f"\n{greeting}, {name}! 👋 Welcome to my GitHub program.\n")

    user_hobby = input("What's one of your hobbies? ").strip().lower()
    
    if not all(x.isalpha() or x.isspace() for x in user_hobby) or user_hobby == "":
        print("Invalid hobby input. Please enter a hobby using letters only.")
        return  

    my_hobbies = ["music", "playing games", "coding", "painting", "swimming", "traveling"]

    print("\nMy hobbies are:", ", ".join(my_hobbies))

    if user_hobby in my_hobbies:
        print(f"Wow! We both enjoy {user_hobby} 🎉")
    else:
        print(f"Nice! {user_hobby} sounds fun too! 😄")

user_name = input("Please enter your name: ").strip()

if all(x.isalpha() or x.isspace() for x in user_name) and user_name != "":
    greet_user(user_name)
else:
    print("Invalid input. Please enter a valid name (letters and spaces only).")

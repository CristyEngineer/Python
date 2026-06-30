# Writing to a file
with open("project.txt", "w") as file:
    file.write("Hello!\nThis is a file handling example.")

# Reading the file
with open("project.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

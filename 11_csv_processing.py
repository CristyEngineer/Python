import csv

print("CSV Processing: Sequential Algorithm Demonstration\n")

filename = "data.csv"

ages = []
people = []

print("Opening the CSV file...\n")

with open(filename, newline="") as file:
    reader = csv.reader(file)

    # Skip header
    next(reader)
    print("People that can drive:")

    for row in reader:
        name = row[0]
        age = int(row[1])
        city = row[2]

        # Loop Control: skip people who cannot drive
        if age < 18:
            continue

        print("Name:", name)
        print("Age:", age)
        print("City:", city)
        print("---")

        ages.append(age)
        people.append((name, age, city))

        # Loop Control: stop after 5 people 
        if len(people) == 5:
            print("Sample size reached. Stopping...\n")
            break

# Filtering: people older than 50 
print("\nPeople older than 50:")
for person in people:
    if person[1] > 50:
        print(person[0], "-", person[1])

# Statistics: calculate average age 
if ages:
    average_age = sum(ages) / len(ages)
    print("\nAverage age:", round(average_age, 2))

# Counting: number of people processed 
print("Number of people processed:", len(people))

# Sorting: people sorted by age 
print("\nPeople sorted by age:")
sorted_people = sorted(people, key=lambda x: x[1])

for person in sorted_people:
    print(person[0], "-", person[1], "-", person[2])

print("\nFinished processing the CSV file.")

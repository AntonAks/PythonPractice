""" Example 1: Checking if a number is positive, negative, or zero: """

num = 10
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


""" Example 2: Determining the grade based on the score: """

score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)


""" Example 3: Checking if a year is a leap year: """

year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


""" Example 4: Checking if a string is empty or not: """
my_string = ""
if len(my_string) == 0:
    print("The string is empty.")
else:
    print("The string is not empty.")


""" Example 5: Checking if a number is divisible by both 2 and 3: """
num = 12
if num % 2 == 0 and num % 3 == 0:
    print(num, "is divisible by both 2 and 3.")
else:
    print(num, "is not divisible by both 2 and 3.")




""" MATCH - CASE """


def identify_fruit(fruit):
    match fruit:
        case "apple":
            print("It's an apple.")
        case "banana":
            print("It's a banana.")
        case "orange":
            print("It's an orange.")
        case _:
            print("It's an unknown fruit.")

identify_fruit("apple")  # Output: It's an apple.
identify_fruit("pear")   # Output: It's an unknown fruit.


def check_number(num):
    match num:
        case 0:
            print("The number is zero.")
        case n if n > 0:
            print("The number is positive.")
        case n if n < 0:
            print("The number is negative.")

check_number(0)    # Output: The number is zero.
check_number(10)   # Output: The number is positive.
check_number(-5)   # Output: The number is negative.


def process_person(person):
    match person:
        case {"name": "Alice", "age": 25}:
            print("Processing Alice...")
            # Perform actions specific to Alice
        case {"name": "Bob", "age": 30}:
            print("Processing Bob...")
            # Perform actions specific to Bob
        case {"name": name, "age": age}:
            print(f"Processing {name} ({age} years old)...")
            # Perform actions for other persons with their name and age
        case _:
            print("Unknown person.")

person1 = {"name": "Alice", "age": 25}
person2 = {"name": "Bob", "age": 30}
person3 = {"name": "Charlie", "age": 35}

process_person(person1)  # Output: Processing Alice...
process_person(person2)  # Output: Processing Bob...
process_person(person3)  # Output: Processing Charlie (35 years old)...



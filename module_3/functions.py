""" Basic function without parameters: """
def greet():
    print("Hello, welcome!")

greet()  # Output: Hello, welcome!


""" Function with parameters: """
def add_numbers(num1, num2):
    sum = num1 + num2
    return sum

result = add_numbers(5, 3)
print(result)  # Output: 8


""" Function with a default parameter: """
def greet(name="Guest"):
    print("Hello,", name)

greet()          # Output: Hello, Guest
greet("Alice")   # Output: Hello, Alice


""" Recursive function: """
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120


""" Function with a variable number of arguments: """
def average(*nums):
    total = sum(nums)
    count = len(nums)
    avg = total / count
    return avg


result = average(2, 4, 6, 8)
print(result)  # Output: 5.0


""" Function with keyword arguments: """
def greet(**kwargs):
    if 'name' in kwargs:
        print("Hello,", kwargs['name'])
    if 'age' in kwargs:
        print("You are", kwargs['age'], "years old")

greet(name="Alice")            # Output: Hello, Alice
greet(name="Bob", age=30)      # Output: Hello, Bob \n You are 30 years old

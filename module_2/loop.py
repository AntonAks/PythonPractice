""" Example 1: for loop iterating over a list: """

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)



""" Example 2: for loop with the range() function: """

for i in range(1, 6):
    print(i)



""" Example 3: for loop iterating over a dictionary: """

person = {"name": "Alice", "age": 25, "city": "New York"}

for key, value in person.items():
    print(key, ":", value)



""" Example 4: while loop: """

count = 0

while count < 5:
    print("Count:", count)
    count += 1


""" Example 5: while loop with a condition: """
num = 10
while num > 0:
    print(num)
    num -= 2


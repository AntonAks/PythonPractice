""" Example 1: Creating a custom iterator: """

class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Usage
my_list = [1, 2, 3, 4, 5]
my_iterator = MyIterator(my_list)

for item in my_iterator:
    print(item)



""" Example 2: Creating a generator function: """
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Usage
fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))



""" Example 3: Using a generator expression: """

my_list = [1, 2, 3, 4, 5]

squared_values = (x ** 2 for x in my_list)

for value in squared_values:
    print(value)

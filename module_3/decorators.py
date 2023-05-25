""" Example 1: Creating a simple decorator: """
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@uppercase_decorator
def say_hello():
    return "Hello, world!"

print(say_hello())  # Output: HELLO, WORLD!


""" Example 2: Decorating a function with arguments: """
def repeat_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 3
    return wrapper

@repeat_decorator
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Output: 15 (3 times the sum of 2 and 3)



""" Example 3: Chaining multiple decorators: """
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@make_bold
@make_italic
def greet():
    return "Hello, world!"

print(greet())  # Output: <b><i>Hello, world!</i></b>



""" Creating a decorator with a parameter: """
def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * times
        return wrapper
    return decorator

@repeat_decorator(times=3)
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))  # Output: 15 (3 times the sum of 2 and 3)


""" Creating a decorator with arguments and using it multiple times: """
def greeting_decorator(greeting):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{greeting} {result}"
        return wrapper
    return decorator

@greeting_decorator(greeting="Hello")
def say_name(name):
    return name

@greeting_decorator(greeting="Bonjour")
def say_age(age):
    return age

print(say_name("Alice"))  # Output: Hello Alice
print(say_age(30))       # Output: Bonjour 30


""" Creating a generic decorator with parameters: """
def parameterized_decorator(param1, param2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Access and use param1 and param2 here
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@parameterized_decorator(param1="Hello", param2=42)
def my_function():
    return "Function output"

print(my_function())  # Output: Function output



""" LIST """

# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [1, 10, 4, 5, 6]


""" TUPLE """

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  # Output: 1

# Modifying elements (not allowed - tuples are immutable)

# Concatenating tuples
new_tuple = my_tuple + (6, 7)
print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)


""" SET """

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
print(union)  # Output: {1, 2, 3, 4, 5}
print(intersection)  # Output: {3}
print(difference)  # Output: {1, 2}


""" DICT """


# Creating a dictionary
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Accessing values
print(my_dict['key2'])  # Output: value2

# Modifying values
my_dict['key1'] = 'new value'
print(my_dict)  # Output: {'key1': 'new value', 'key2': 'value2', 'key3': 'value3'}

# Adding new key-value pairs
my_dict['key4'] = 'value4'
print(my_dict)  # Output: {'key1': 'new value', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

# Removing key-value pairs
del my_dict['key3']
print(my_dict)  # Output: {'key1': 'new value', 'key2': 'value2', 'key4': 'value4'}



""" Queue 1 """

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.size())  # Output: 2


""" Queue 2 """

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.size())  # Output: 2


if __name__ == '__main__':
    pass

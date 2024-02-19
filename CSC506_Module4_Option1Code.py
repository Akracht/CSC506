#Import Statements
import random
from collections import deque
import timeit


#List-Based Stack
class PythonListStack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, item):
        # Add an element to the top of the stack
        self.stack.append(item)

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def peek(self):
        # Return the top element of the stack without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        # Return the number of elements in the stack
        return len(self.stack)

#List-Based Queue
class PythonListQueue:
    def __init__(self):
        # Initialize an empty deque to store queue elements
        self.queue = deque()

    def enqueue(self, item):
        # Add an element to the rear of the queue
        self.queue.append(item)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def peek(self):
        # Return the front element of the queue without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def size(self):
        # Return the number of elements in the queue
        return len(self.queue)

#Linked-List Stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

#Linked List Queue
class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

#Analytics Definitions
# Function to generate random integers
def generate_random_integers():
    return [random.randint(1, 100) for _ in range(10)]

# Function to measure average execution time of each method
def measure_average_time(data_structure, operation, iterations):
    total_time = 0
    for _ in range(iterations):
        random_integers = generate_random_integers()
        start_time = timeit.default_timer()
        operation(data_structure, random_integers)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)
    return total_time / iterations



# Function to perform stack operations
def perform_stack_operations(data_structure, random_integers):
    for num in random_integers:
        data_structure.push(num)

# Function to perform queue operations
def perform_queue_operations(data_structure, random_integers):
    for num in random_integers:
        data_structure.enqueue(num)


#Sample Data & Initialization
# Generate 10 random integers
random_integers = [random.randint(1, 100) for _ in range(10)]
# Define iterations
iterations = 1000

#Generate Data Structures
# Create a stack and push the random integers onto it
stack = PythonListStack()
for num in random_integers:
    stack.push(num)

# Create a queue and enqueue the random integers onto it
queue = PythonListQueue()
for num in random_integers:
    queue.enqueue(num)

# Create a linked list stack and push the random integers onto it
linked_stack = LinkedListStack()
for num in random_integers:
    linked_stack.push(num)

# Create a linked list queue and enqueue the random integers onto it
linked_queue = LinkedListQueue()
for num in random_integers:
    linked_queue.enqueue(num)

# Measure average execution time for each method - Generating stack or queue
stack_push_time = measure_average_time(PythonListStack(), perform_stack_operations, iterations)
queue_enqueue_time = measure_average_time(PythonListQueue(), perform_queue_operations, iterations)
linked_stack_push_time = measure_average_time(LinkedListStack(), perform_stack_operations, iterations)
linked_queue_enqueue_time = measure_average_time(LinkedListQueue(), perform_queue_operations, iterations)

# Create a dictionary to hold the execution times
execution_times = {
    "Python List Stack (push)": stack_push_time,
    "Python List Queue (enqueue)": queue_enqueue_time,
    "Linked List Stack (push)": linked_stack_push_time,
    "Linked List Queue (enqueue)": linked_queue_enqueue_time
}

# Rank the execution times
ranked_times = sorted(execution_times.items(), key=lambda x: x[1])

# Print the ranked execution times
print("Ranked Average Execution Times (seconds) for 1000 iterations - Generate Stack / Queue of 10 elements :")
for i, (method, time) in enumerate(ranked_times, start=1):
    print(f"{i}. {method}: {time}")



#Print Data Structure Content
# Print the stack contents
print("List Based Stack contents:")
while not stack.is_empty():
    print(stack.pop())

# Print the queue contents
print("List Based Queue contents:")
while not queue.is_empty():
    print(queue.dequeue())

# Print the list based stack contents
print("Linked-List Based Stack contents:")
while not linked_stack.is_empty():
    print(linked_stack.pop())

# Print the linked-list queue contents
print("Linked-List Based Queue contents:")
while not linked_queue.is_empty():
    print(linked_queue.dequeue())











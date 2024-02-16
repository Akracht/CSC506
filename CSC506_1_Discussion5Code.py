import time
import random

# Establish Hash Table
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize table as a list of empty lists

    def _hash_function(self, key):
        return key % self.size  # Simple hash function to map keys to indices

    def insert(self, key, value):
        index = self._hash_function(key)  # Get index using hash function
        self.table[index].append((key, value))  # Append key-value pair to the corresponding bucket

    def get(self, key):
        index = self._hash_function(key)  # Get index using hash function
        bucket = self.table[index]  # Get the bucket at the calculated index
        for k, v in bucket:
            if k == key:
                return v  # Return the value if key is found
        raise KeyError("Key not found")  # Raise an error if key is not found

# Initialize
used_slots = 0
iterations = 1000000

student_dict = {}  # Initialize dictionary

studentID = {
    12345: "John Smith",
    67890: "Jane Doe",
    54321: "Alice Johnson",
    98765: "Bob Williams",
    24680: "Eve Brown",
    13579: "Charlie Davis",
    11223: "Grace Wilson",
    44556: "David Lee",
    99999: "Olivia Martinez",
    77777: "Sophia Anderson"
}

# Store Student ID Key, value pairs as dictionary elements
for key, value in studentID.items():
    student_dict[key] = value

# Generate student ID -> name hash table and populate w/ studentID key value pairs
student_hash = HashTable(size=10)
for key, value in studentID.items():
    student_hash.insert(key, value)

# Choose random studentID from list
randID = random.choice(list(student_dict.keys()))  # Choose a random key from dictionary to retrieve and test against hash time

# Main()
hash_total_time = 0
dict_total_time = 0

for _ in range(iterations):
    tic = time.time()
    student_hash.get(randID)  # Hash table method
    toc = time.time()
    hash_total_time += toc - tic #Sum of time taken over all iterations

    tic = time.time()
    student_dict[randID]  # Dictionary Method
    toc = time.time()
    dict_total_time += toc - tic #Sum of time taken over all iterations

# Calculate average times
avg_hash_time = hash_total_time / iterations 
avg_dict_time = dict_total_time / iterations

print(f'Average time for hash table method: {avg_hash_time} seconds')
print(f'Average time for dictionary method: {avg_dict_time} seconds')

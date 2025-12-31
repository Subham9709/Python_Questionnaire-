# Demonstration of five list methods in a single program

numbers = [3, 1, 4]

# 1. append()
numbers.append(2)          # adds 2 at the end
# list becomes [3, 1, 4, 2]

# 2. insert()
numbers.insert(1, 5)       # inserts 5 at index 1
# list becomes [3, 5, 1, 4, 2]

# 3. remove()
numbers.remove(1)          # removes first occurrence of 1
# list becomes [3, 5, 4, 2]

# 4. pop()
numbers.pop()              # removes last element
# list becomes [3, 5, 4]

# 5. sort()
numbers.sort()             # sorts the list in ascending order

print(numbers)
# Final list after all operations: [3, 4, 5]    
"""Test TASK 2 binary_search"""

from binary_search import binary_search

test_array = [-1, 1, 2, 3, 4, 10.5, 40]
print(f"{test_array = }")
print(f"{len(test_array) = }")
x = 3.7
result = binary_search(test_array, x)
if result[1]:
    print(f"Result is {result}")
else:
    print("Required element was not found in array")

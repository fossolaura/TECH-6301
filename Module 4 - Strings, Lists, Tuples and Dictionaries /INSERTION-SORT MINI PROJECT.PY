# Requirements
#The Insertion-sort function involves finding the correct place for a given element in a sorted list. This process begins with comparing and sorting the first two elements. A third element is then compared to the two previously sorted elements and found its proper position among them. This way, more elements gradually added to a continuously sorted list by inserting them into their proper positions. Write a program that sorts an array using the insertion-sort algorithm.

import random

# Step 1: Create a random list of numbers
# Generating a list of 10 random numbers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

# Step 2: Apply the Insertion Sort algorithm
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

# Sorting the list
insertion_sort(random_list)

# Step 3: Print the sorted list
print("Sorted list:", random_list)

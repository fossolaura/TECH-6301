# Requirements
# Merge-sort first divides the array into equal halves, then combines them in a sorted manner. Write a program that sorts the array using merge-sort algorithm.
import random

# Step 1: Create a random list of numbers
# Generating a list of 10 random numbers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

# Step 2: Define the Merge Sort algorithm
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting the first half
        merge_sort(L)
        
        # Sorting the second half
        merge_sort(R)
        
        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Step 3: Sort the list and print the sorted list
merge_sort(random_list)
print("Sorted list:", random_list)

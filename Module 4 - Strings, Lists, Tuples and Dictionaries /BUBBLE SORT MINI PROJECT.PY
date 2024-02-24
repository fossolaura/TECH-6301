import random

# Step 1: Create a random list of numbers
# Generating a list of 10 random numbers between 1 and 100
random_list = [random.randint(1, 100) for _ in range(10)]
print("Original list:", random_list)

# Step 2: Apply the Bubble Sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True
        
        # Compare each item to its neighbor
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # Since we had to swap, we can't be sure if the list is
                # already sorted and must continue
                already_sorted = False
        
        # If there were no swaps during the last iteration,
        # the array is already sorted, and we can exit
        if already_sorted:
            break

    return arr

# Sorting the list
sorted_list = bubble_sort(random_list)

# Step 3: Print the sorted list
print("Sorted list:", sorted_list)
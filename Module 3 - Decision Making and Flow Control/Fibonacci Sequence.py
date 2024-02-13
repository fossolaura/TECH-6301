#  The Fibonacci Sequence


# Required variables
prev_num = 0
current_num = 1

# Input from the user
num_fibonacci = int(input("How many Fibonacci numbers would you like to generate? "))

# Ensure posotive number inputs only
if num_fibonacci <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for _ in range(num_fibonacci):
        print(prev_num, end=' ')
        next_num = prev_num + current_num
        prev_num = current_num
        current_num = next_num


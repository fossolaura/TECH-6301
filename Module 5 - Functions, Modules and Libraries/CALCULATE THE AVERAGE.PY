#Requirements
#Write a function to calculate the average of the numbers in a list of items using the built-in sum functio

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The average is:", calculate_average(numbers))

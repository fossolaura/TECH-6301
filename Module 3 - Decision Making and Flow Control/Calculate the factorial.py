#Requirements
#Write a program that calculates the factorial of a number given by the user, then prints the output.

# Take the required input from the user
num = int(input("Enter a number to calculate the factorial: "))

factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")

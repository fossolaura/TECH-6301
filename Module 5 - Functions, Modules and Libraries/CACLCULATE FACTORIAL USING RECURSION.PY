#Requirements
#Write a function to calculate factorials using recursion.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = 7
print(f"The factorial of {number} is:", factorial(number))

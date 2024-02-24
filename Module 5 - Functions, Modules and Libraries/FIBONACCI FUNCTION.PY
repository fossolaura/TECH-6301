#Requirements
#Write the Fibonacci function you wrote in the last submodule, but this time with recursion.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci number at index 10:", fibonacci(10))

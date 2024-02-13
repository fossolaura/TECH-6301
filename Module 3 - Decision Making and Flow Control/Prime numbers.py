# Requirements
#Write a program to print all the prime numbers between 2 and a number (N) given by the user.


N = int(input("Enter a number to find all prime numbers up to: "))

print(f"Prime numbers between 2 and {N} are:")
for num in range(2, N + 1):  
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):  
        if num % i == 0:  
            is_prime = False
            break
    if is_prime: 
        print(num, end=' ')

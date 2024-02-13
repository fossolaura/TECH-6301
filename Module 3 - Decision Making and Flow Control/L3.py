# MODULE 3: DECISION MAKING & FLOW CONTROL
# What I will learn in this lesson?
#   In this lesson, I will be introduced to multiple methods of decision-making. By the end of this lesson, I will be able to
#       Define multiple methods of decision-making, like "if" statements, "if...else" statements, and nested "if" statements; and
#       Define the "match case" statement in Python.

# Decision making in code is enssentially like making code for every possible
# scenario the user can take.

# If statement
# used if you want to run a specific block when a specific condition is fulfilled. The syntax of the if statement is as follows:
# note the idention: everything condition under the same indentation is known as a code block

x=10 

if x>15: 

    print("x is greater than 15") 

if x>5: 

    print("x is greater than 5") 


# if...else statements
# The if...else statement is like the if statement, except that the code block inside else clause is executed when the condition of the if statement is not fulfilled (is false).    

a= 10  

if a>20: # condition is False, the code block inside else statement will be executed 
    
    print("a is greater than 20")  

else:  

    print("a is lower than 20")    


# elif statement
# The elif statement can be added to the if..else statement to assess numerous expressions for truthfulness and executing a code block as soon as any conditions are true. It is worth noting that the elif statement can come multiple times after the if statement, unlike the else clause, which can only be stated once.
# The syntax of the if...elif...else statement is as follows:   

grade=67 

if grade > 85: 

    print("Excellent") 

elif grade>75: 

    print("Very good") 

elif grade>65: 

    print("Good") 

elif grade>50: 

    print("Pass") 

else:  

    print("Failed") 

print("Good luck")   


# Nested if statements
# A scenario might arise where you need to verify an extra condition after the resolution of a previous true condition. In such cases, the option of employing a nested if structure is available. Within a nested if structure, it is possible to include one if...elif...else construction inside another.
# The syntax of a nested if statement is as follows:

x=50 

if x<60: 

    print("x is less than 60") 

    if x>55:  

        print("x is greater than 55") 

    elif x==50: 

        print("x equals 50") 

     

    elif x>45: 

        print("x is greater than 45") 

    else: 

        print("x is less than 45") 

else: 

    print("x is greater than 60") 
  
print("Bye bye")

# The match case statement in Python
# allows you to control the flow of your programs more easily by executing certain parts of your code if conditions (or cases) are met.
# The basic implementation of a match case statement looks a lot like an if statement in Python. However, Python’s match case statement 
# in is more powerful and allows for more complicated pattern matching.


# EDITOR: DECISION-MAKING

# Instructions:

# To complete this activity, perform the following tasks: 
# Complete this code snippet to check if a number is divisible by 7. 
# Your code should return True if the number is divisible by 7; otherwise, it should return False. 

# Hint: If the number is 49, it will be divisible by 7 because the reminder value of the division between 49 and 7 is 0. If the remainder is not 0, the number will not be divisible by 7. 
def main():
    num = 20

    # Check if num is divisible by 7
    divisible = (num % 7 == 0)

    return divisible

# Call the main function and print the result
print(main())

#Instructions:

# To complete this activity, perform the following tasks: 
# Write a Python code to check if the last digit of the variable num is divisible by 3. 
# Your code should return True if the last digit is divisible by 3; otherwise, it should return False.  

# Hint:  
# The last digit of a number is computed by utilizing the operation of the reminder 10 (%10) of the number. For example, if the number is 2789, the last digit will be calculated as follows: 
#               Last digit= 2789%10= 9 
def main():  

    num=27   

    ## Type your code here  
    divisible = ((num % 10) % 3 ==0)
    # divisible 
    return divisible  

print(main()) 

# In this lesson, you will be introduced to different types of flow control. By the end of this lesson, you will be able to
#   Identify different types of flow control; and
#   Identify and use control statements.

# THE WHILE LOOP
# repeatedly executes a task, if the loop condition is achieved.
# The syntax of the while loop is as follows:
#   while condition:  
#   code block 
i=5  
while i>0: 
    break # dont want the continue to continusly run every time i run the code
    print("i=",i) 
    i-=1 
print("Good bye")


# INFINITE LOOP
# A loop transforms into an infinite loop when a condition remains perpetually True.
while True:  
    break
    print("Hello World")

# WHILE...ELSE STATEMENTS
# When else is employed in conjunction with while, the code segment within the else statement 
# will be executed once the condition of the while loop transits from True to False.    
num=10 
while num > 5: 
    break
    print("Inside the loop, num:", num) 
    num-=1 

else: 
    print("Outside the loop, num:", num)    

# SINGLE STATEMENT
# if your while clause consists only of a single statement, it may be placed on the same 
# line as the while header

while True: 
    print("hello World") 
    break
print("Bye bye")

# FOR LOOP

# Python loop that is utilized for iterating through a sequence, such as a list, tuple, dictionary, set, or string.
ls= [7,"Hello", 2.5] 

st="RoboGarden" 

for item in ls: #iterate over a list 

    print("item:", item) 

for letter in st: 

    print("letter:", letter)

# THE ELSE STATEMENT AND THE FOR LOOP
# Similar to the while loop, when the else statement is employed in conjunction with a for loop, 
# the code controlled by else is executed after the loop has finished iterating through a sequence.
st="Robo" 

for ind in range(len(st)): 

    print("ind:", ind, "letter:", st[ind]) 

else: 

    print("No other letters in st")

# NESTED LOOP
tp=("hello","hi","Robo") 

for i in range(len(tp)): 

    print("tuple index:", i, "tuple item:", tp[i]) 

    for letter in tp[i]: 

        print("letter:", letter) 

# CONTROL STATEMENTS

#Python incorporates the following control statements:
#   Break: This control statement concludes the loop's execution and transfers control to the statement that follows the loop.
#   Continue: This control statement causes the loop to bypass the remaining part of its body and promptly reevaluate its 
#               condition before initiating the next iteration.
#   Pass: This control statement serves as a void action; no actions are taken upon its execution. Moreover, it proves 
#               beneficial in situations where your code will eventually be written, but currently remains unwritten.

# ACTIVITY
# Instructions: 

# To complete this activity, perform the following tasks: 
#Complete this code snippet to calculate the average value of a list.  

#For example: 
#If the list is [1,8,9], 
#The average = (sum values of the list) / (number of list’s items)  
#Average= (1+8+9)/3= 6 

def main(): 

    ls=[2,7,4,6,2] 

    ## Type your code here 

    average=  sum(ls) / len(ls)

    ##################### 

    return average 

print(main()) 

# Instructions:

# To complete this activity, perform the following tasks:  
# Write a Python code to get the index of the first odd number in the list, ls.  

# Hint: 
# The odd number is a number not divisible by 2. 
# For example, 11 is considered odd because when you divide it by 2, 
# the remainder is not 0 (11%2!= 0). 
def main():  

    ls=[2,8,6,5,2,7,9]   

    ## Type your code here 
    index = -1
    #####################  
    for i in range(len(ls)):
     if ls[i] % 2 != 0:
        index = i
        break
    return index  

print(main()) 
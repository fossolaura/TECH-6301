# MODULE 2: PYTHON BASICS

#What I you learn in this lesson?

#   In this lesson, I will be introduced to the fundamentals of the syntax of the Python programming language.
#   By the end of this lesson, I will be able to: 
#       - Write Python syntax, including indentation, quotations, and comments; and
#       - Read keyboard inputs.


# QUOTATION
# 3 types of quotations in Python
# Single
print('hello everyone') 
# Double
print("hello everyone")  
# Triple : can also be used to recognize multi-line strings, which the latter two types of mark cannot identify.
print('''hello everyone''')  
print("""hello everyone""") 
print('''hello everyone I hope you are well. 
      Welcome to RoboGarden 
      course''') # example of a multi-line string (this is an example of an inline comment)


# COMMENTS
# Serve as explanatory or annotative text 
# is disregarded by the Python interpreter
# Ex: All of my notes will be considered "comments" in a code. (this is an example of a standalone comment)
# '''when a comment spans on
#      multiples lines and is withing 
#       triple quotes''' is is know was as a Multi-line comment.


# VARIABLES
# An unknow entity with a custom name of my choosing thats holds value
# There are no requirements for a delibrate declaration of variables to be allocated memory space.
# value assign using = sign.
# Variables name = value of variable
#      Ex: 
a = 2          # a is an integer (whole number, positive or negative variable
b = 2.0        # b is a float (Decimals, positive or negative) variable
c = "hi"       # string (text) variable

#Characteristic if a good variable name 

# The first character of a variable name must be either a letter or the underscored symbol.
# A variable name cannot commence with a numeral or any special character, like $, (, *, %, etc.
# A variable name may exclusively encompass alphanumeric characters and underscores (A-Z, 0-9, and _).
# It is imperative to note that Python variable names are case sensitive; hence, Name and NAME are recognized as distinct variables within Python.
# Python's reserved keywords cannot be employed for naming variables. You can find all Python’s reserved words in the table below.
#       `if`, `else`, `elif`, `while`, `for`, `break`, `continue`, `return`, `yield`, `try`, `except`, 
#       `finally`, `import`, `from`, `as`, `def`, `class`, `with`, `lambda`, `nonlocal`, `global`, `assert`,
#       `async`, `await`, `pass`, `raise`, `del`, `is`, `not`, `or`, `and`, `True`, `False`, `None`.

#to delete a variable 
del a
##del a, b, c

#to define multiple variables
a = b = c = 10


#IDENTATION
# Code blocks pertaining to class and function definitions or flow control are delineated through the use of line indentation - VERY IMPORTANT
# All statements within a given block MUST possess uniform indentation
# Definition: a block is a series of consecutive lines that share an identical level of indentation.
# EX:
if True:  
     print("True") 
else:  
     Print("False") 
print('hello world')


#READING KEYBOARD INPUTS

#user inputs are returned as string with the input() fxn
#Ex:

Name = input("What's your name:")
print("My name is:", Name)


#NUMERICAL DATA TYPES 
# int: integer values that don’t have a floating point (e.g. 2).
# long: long integer value.
# float: numbers with floating points, such as 2.3.
# complex: complex numbers, like 2+3j.

# You can check the type of variable by printing the type fxn
a=3  #class 'int'
b=2.1 #class 'float
c=3+4j #class 'complex'

print(type(a))
print(type(b))
print(type(c))


#STRING DATA TYPE
# consecutive sequences of characters encapsulated within quotation 
# Single, double, and triple quotes


# LIST DATA TYPE
# Incredible versatile data structures
# various items are grouped together, separated by commas, and enveloped within square brackets ([])
#Ex: 
ls1= [ 'abcd', 786 , 2.23,'lj']
ls2 = [20, 'garden']

print(ls1) #['abcd', 786, 2.23, 'lj']
print(ls1[1]) #786 
print(ls1[0:3]) #['abcd', 786, 2.23]
print(ls1[2:]) #[2.23, 'lj'] - so print 1 onward
print(ls1*2) #['abcd', 786, 2.23, 'lj', 'abcd', 786, 2.23, 'lj']
print(ls1+ls2) #['abcd', 786, 2.23, 'lj', 20, 'garden']


# TUPLE DATA TYPE
# An alternative sequence data structure akin to lists
# Multiple values separated by commas contained within parentheses.
# Cannot be modified.
# Ex: 
tp= (2,"john", 5.6)
ls = [10,"abcd", 2.1]

print(tp) #(2, 'john', 5.6)
print(ls) #[10, 'abcd', 2.1]

ls[1]=20
print(ls) 
#[10, 20, 2.1] - Assigned 20 to the 1st place in the list hereby replacing john

##tp[1]=20
##print(tp)
#TypeError: 'tuple' object does not support item assignment


# DICTIONARY DATA TYPE
# Consist of pairs of keys and their corresponding values
# Can encompass an array of different types
# Dictionaries are characterized by curly brackets ({}) that enclose their key-value pairs. 
#   The values can be accessed and assigned via square brackets ([]).
# Ex:
dt = {} #Dictionary
dt['A'] = "all people" #key
dt[2]   = "number two" #key
 
print (dt['A'])     # all people - prints value for 'A' key
print (dt[2])       # number two - Prints value for 2 key
print(dt.keys())    # dict_keys(['A', 2]) - prints all keys
print(dt.values())  # dict_values(['all people', 'number two']) - print all values


# BOOLEAN DATA TYPE
# Signifies one of two possible values: True or False
# The bool() function, which permits the assessment of any given expression 
# and yields either True or False in accordance with the expression's evaluation.
# Ex:
a = True 
print(type(a)) #<class 'bool'>

x = 2
y = 3
print(bool(x==y)) #False


# NONE DATA TYPE
# Denote a null value or a null object
# It differs from an empty string, a false value, 
# or a 0 in that it represents the absence of a value.
#Ex:
my_variable = None
print(my_variable) # None


# DATA TYPES CONVERSION
# To transition data among various Python data types, 
# use the type name as this functions as a conversion tool.
#Ex:
a=int("123")  # Converts the string "123" to the integer 123
print(a)

b=str(123)  # Converts the integer 123 to the string "123"
print(b)

c=float("123.45")  # Converts the string "123.45" to the float 123.45
print(c)

d=int(123.45)  # Converts the float 123.45 to the integer 123
print(d)


# PYTHON OPERATORS


# Arithmentic operators
# used for performing mathematical operations on variables
# Addition (+), Subtraction (-), Multiplication (*)
# Division (/), Modulus (%), Exponent (**), Floor division (//)
# Ex:
a = 5
b = 3

print("Addition:", a + b)        # Prints the result of a + b
print("Subtraction:", a - b)     # Prints the result of a - b
print("Multiplication:", a * b)  # Prints the result of a * b
print("Division:", a / b)        # Prints the result of a / b
print("Modulus:", a % b)         # Prints the remainder of a / b
print("Exponent:", a ** b)       # Prints a raised to the power of b
print("Floor Division:", a // b) # Prints the integer part of a / b

# Assignment operators 
# used for performing assignment operations on variables

x = 10            # Assignment
print("x:", x)

x += 3            # Addition assignment: increase x by
print("x += 3:", x)  # x is now 13

x -= 1            # Subtraction assignment: decrease x by
print("x -= 1:", x)  # x is now 12

x *= 2            # Multiplication assignment: make x bigger by
print("x *= 2:", x)  # x is now 24

x /= 3            # Division assignment: divide x by
print("x /= 3:", x)  # x is now 8.0

x %= 5            # Modulus assignment: divide x by and keep remainder
print("x %= 5:", x)  # x is now 3.0 (8 modulo 5 is 3)

#    mini tuto on mods
#    8 mod 5 = 
#         8/3 = 1 R3 ( 1 remainder 3)
#         now put answer in the equation
#         quotien * divisor + remainder = divident
#              1  *     5   +  3        =  8
#         the remainder (R3) is the answer.
x **= 2           # Exponent assignment: exponent x by
print("x **= 2:", x)  # x is now 9.0

x //= 2           # Floor division assignment: divide x by and round to the nearest whole number
print("x //= 2:", x)  # x is now 4 (9 divided by 4 and rounded down)

# TO REMEMBER: if you want the value of x to be static through out the code,
#    you hae to restarted the value of x before each operations.

# Comparaison operators 
# also know was relations operators, theuy assess the values
# on both side of the operator and determine a relationship between them.

a = 10
b = 20

print("Is a equal to b?", a == b)  # False, because 10 is not equal to 20
print("Is a not equal to b?", a != b)  # True, because 10 is not equal to 20

print("Is a greater than b?", a > b)  # False, because 10 is not greater than 20
print("Is a less than b?", a < b)  # True, because 10 is less than 20

print("Is a greater than or equal to b?", a >= b)  # False, because 10 is neither greater than nor equal to 20
print("Is a less than or equal to b?", a <= b)  # True, because 10 is less than 20

# Logical operators
# are used to combine conditional statements
# apdopte Boolean logic
x = 7
y = 10

# AND operator
print("x > 5 and y > 5:", x > 5 and y > 5)  # True, because both conditions are true
# 7 > 5 and 10 > 5: True
# OR operator
print("x > 10 or y > 5:", x > 10 or y > 5)  # True, because one condition (y > 5) is true
# 7 > 10 or 10 > 5: True
# NOT operator
print("not(x > 5):", not(x > 5))  # False, because x > 5 is true, and not(True) is False
# not(7 > 5): False

# Bitwise operators
# work on numerical values but treat it as a sequence of individual bits (zeros and ones).
# Hence the operands undergo automatic conversion into binary buts in order for the operation
# to be carried out.
# Once the operation is completed, the resulting bits are reocnverted into numerical values.
# *REMEMBER*
#     The bits of a number are predetermined. 

# Binary AND (&) Results 1 if both operands’ bits are 1, otherwise results 0.
a = 5  # 5 in binary is 101
b = 3  # 3 in binary is 011
print(a & b)  # Outputs 1 (binary 001) - see xplanation below

# a = 5 which in binary is 101.
# b = 3 which in binary is 011.
# The bitwise AND operation compares each corresponding bit of these binary numbers:
# keep in mind the comparison is done from right to left
#    First bit: 1 (from 101) AND 1 (from 011) gives 1.
#    Second bit: 0 (from 101) AND 1 (from 011) gives 0.
#    Third bit: 1 (from 101) AND 0 (from 011) gives 0.
# So, the result of 101 AND 011 is 001, which is 1 in decimal (equivalent value in the decimal number system). 
#    That's why print(a & b) outputs 1.

# Binary OR (|): Results 1 if one of the two operands’ bits is 1, otherwise results 0.
a = 5  # 5 in binary is 101
b = 3  # 3 in binary is 011
print(a | b)  # Outputs 7 (binary 111)

# Binary XOR (^): Results 1 if only one of the two operands’ bits is 1, otherwise results 0.
a = 5  # 5 in binary is 101
b = 3  # 3 in binary is 011
print(a ^ b)  # Outputs 6 (binary 110)

# Binary Ones complement or Binary NOT (~): Inverts bits from 1 to 0 and vice versa.
a = 5  # 5 in binary is 101
print(~a)  # Outputs -6 (in binary, this is the two's complement of 101)

# Explanations:
# In binary, 5 is represented as 101. In an 8-bit system, it's 00000101.
# The ~ operator inverts all bits. So 00000101 becomes 11111010.
# In binary, negative numbers are represented using two's complement. To find the two's complement:
#   First, invert all the bits (which ~ already does).
#   Then, add 1 to the result.
# So, after inverting, you have 11111010 (6 in decimal). Add 1 to this, you get 11111011.
# 11111011 is the two's complement representation of -6.

# Binary Left Shift (<<): Left shifting involves introducing 0 from the right side, causing the leftmost bits to be displaced or dropped.
a = 5  # 5 in binary is 101
print(a << 1)  # Outputs 10 (binary 1010)

# Binary Right Shift (>>): Right shifting entails inserting duplicates of the leftmost bit from the left side, leading to the removal of the rightmost bits.
a = 5  # 5 in binary is 101
print(a >> 1)  # Outputs 2 (binary 10) essentialy the 1 (leftmost bit) was dropped.

#  Membership operators 
# assess whether an element belongs to a sequence, like strings, lists, or tuples. These operators are:

a= 10
b=20
ls=[12,10, "hello"]
tp= ("hi", 1,20)

# Operator (in): Results in a True outcome if a variable is discovered within the indicated sequence; otherwise, it yields False.
print("a in ls:", a in ls) # a in ls: True
print("b in ls:", b in ls) # b in ls: False

# Operator (not in): Performs the reverse operation of the operator (in).
print("a not in tp:", a not in tp) # a not in tp: True
print("b not in tp:", b not in tp) # b not in tp: False

# Identity operators
# compare objects, verifying whether or not both objects are genuinely of the same data type and share identical memory locations
a= 10
b= 10
c= 4 
# Operator (is): Returns True if both variables point to the same object.
print("a is b:", a is b) # a is b: True
print("id(a)==id(b):", id(a)==id(b)) # id(a)==id(b): True

print("a is c:", a is c) # a is c: False
print("id(a)==id(c):", id(a)==id(c)) # id(a)==id(c): False

# Operator (is not): eturns True if the variables do not point to the same object.
print("b is not  a:", b is not a) # b  is not a: False
print("id(a)!=id(b):", id(a)!=id(b)) # id(a)!=id(b): False
 
print("b is not c:", b is not c) # b is not  c: True
print("id(a)!=id(c):", id(a)!=id(c)) # id(a)!=id(c): True


# MISSION: To complete this activity, perform the following: 
# Complete the code snippet on the left to return the variable c 
# by adding the numbers (an and b) and then convert the result to a string data type.

def main():
    a=10
    b=3.6
    
    ## Uncomment the line below and type your code
    c=str(( a + b))

    return c
results = main ()
print(main())
print(type(results))


# MISSION: To complete this activity, perform the following: 
# - Write a Python code that increments the variable “a” by 4 and subsequently applies an XOR operation with 2.
# - After these consecutive operations, return the updated value of the variable "a." 

def main():  

    a=3 

    a+=4 

    a^=2

    #############  

  

    return a  

print(main())

# MISSION QUIZ

# What data type stores only the two values: True or False? 
#         BOOLEANS
#         Confident

# Can a tuple’s items be changed after creation?
#         NO,tupes are immutable in python
#         Confident

# Which logical operator reverses the logical state of a statement?
#         Not
#         Confident








# LET'S DO THE MINI PROJECT
# Calculate Age
     # Requirements
     # Write a program to calculate age of a person/item. 
     #The program takes two inputs from the user(year person born/item created and current year) and prints out the age of the person/item.

print("I'm going to calculate your age")

print("I need 2 inputs from you")

Year_born = input("What year were you born?: ")
Current_year = input("What year are you in right now?: ")

Year_born_int =int(Year_born)
Current_year_int = int(Current_year)

Age = (Current_year_int - Year_born_int)

print(f"You are", Age, "years old !")


# Calculate Age - Questionnaire

# 1. What is the primary objective of this mini-project?
# write a program that print age

# 2. How many inputs does the program require from the user?
#  2

# 3. What type of information is required from the user to calculate age?
#  Year of birth and current year

# 4. What is the expected output of this program?
#  the age of the persom/item

# 5. In the context of the project, what do the user inputs represent?
#   Born/created year and current year

# 6. Which function is commonly used to take user input in Python?
#    input ()

# 7. What is the purpose of subtracting the born year from the current year in the program?
#    To find the age of the person.

# 8. What will the program do if a user mistakenly enters a letter instead of a number for the born year?
# Print an error message and terminate the program.
# could also use a while loop --- but have not learned that yet in this course.

# 9. Which line of code will output the calculated age using the print() function? choose the best one 
#    all of the above

# 10. What does the term "input validation" do in the context of this mini-project?
#    Verifies the user input to ensure it meets specified criteria.





# LET'S DO THE MINI PROJECT
# Calculator
# Requirements
#    In this assessment, you will create a calculator. Write a program that gets two inputs from the user 
#    and performs basic calculator functionalities on them (add, subtract, multiply and divide).


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
# Assignment operator (=), Addition assignment (+=), Subtraction assignment (-=)
# Multiplication assignment (*=), Division assignment (/=), Reminder assignment (%=)
# Exponent assignment (**=), Floor division assignment (//=)


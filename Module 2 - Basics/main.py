# LET'S DO THE MINI PROJECT
# Calculate Age


print("I'm going to calculate your age")

print("I need 2 inputs from you")

# Take the first input from the user and call it start_year.

start_year = input("What year were you born?: ")
start_year_int =int(start_year)

# Take the second input from the user and call it end-year.
end_year = input("What year are you in right now?: ")
end_year_int = int(end_year)

# Create a variable age and assign it to the calculated age from the two inputs.
age = (end_year_int - start_year_int)

# Print the age variable.
print(f"You are", age, "years old !")



# LET'S DO THE MINI PROJECT
# Calculator

# Take the first input from the user and call it first_number.
first_number = int(input("Enter your first number: "))

# Take the second input from the user and call it second_number.
second_number = int(input("Enter your second number: ")) 

# Create the variables sum, subtraction, multiplication and division and assign them their values based on the two inputs.
a = first_number
b = second_number

"Addition:", (a + b)        
"Subtraction:", (a - b)     
"Multiplication:", (a * b) 
"Division:", (a / b) 

# Print the four variables.
print("Addition:", a + b)        
print("Subtraction:", a - b)     
print("Multiplication:", a * b) 
print("Division:", a / b) 
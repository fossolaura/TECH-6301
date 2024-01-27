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
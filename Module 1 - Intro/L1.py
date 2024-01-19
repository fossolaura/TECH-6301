#The print function

print ("Hello World.")

#Integrated Development Environment (IDE)
    #Python can be executed without a terminal by making use of IDEs such as PyCharm or VS Code.
        #combine code editing and execution
        #can avoid the potential issue of providing an incorrect file path

#Instructions:
    #To complete this activity, perform the following task: Write a Python code that defines a variable named “x”, 
    #and assign it the string value, “Welcome to the RoboGarden course.”. Then print the variable.  
X = "Welcome to the RoboGarden course"
print(X)
    #Tried 3/4 times. I was forgetting the period (.) at the end of string.
#Right Version
x = "Welcome to the RoboGarden course."
print(x)

#IN CLASS LESSON NOTES - 06/01/2024

#When writing variable you can call them X,Y,Z
#but is recommended to name the variable by its name.
    #Example Name = "Enter a name"
            #Name_of_the_user = "Enter a name"  

#Whenever there's a sliggly line, that means there a syntax error.

#Input fx : Waits for an input from the user

name = input("please write your name:")
print (name)

#Concatinating strings
name = input("please write your name:")
print ("Hello," + name)

#this doesnt work becasue the user input will be converted to a string
number = input("Please enter a number: ")
print(number*2)
#So the answer we will get here will be 33 and not 6

#In order to get a 6, you need to define your input as an interger
number = int(input("Please enter a number: "))
print(number*2)

#End of course for day 1
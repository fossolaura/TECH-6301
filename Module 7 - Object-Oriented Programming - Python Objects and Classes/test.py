def main():

    class Person:

        def __init__(self, name, age):
            self.name = name
            self.age = age

    ## Type your code below to complete the Student class creation
    class Student(Person):

        def __init__(self, name, age, id):
            super().__init__(name, age)  # Initialize the superclass with name and age
            self.id = id  # Define a new attribute for the Student class

    ##########

    obj1 = Student("John", 23, 1234)  # object instance from the Student class

    ## Type your code to get the attributes dictionary for the obj1
    dict_att = obj1.__dict__

    ############################
    print(dict_att)

    return dict_att

main()

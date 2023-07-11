# Classes are mould/blue prints in our code to create our own datatypes called objects
# Classes are immutable but we can make them mutable so two in one
# Classes come with certain methods that we can define and made them act certain way
class Student:   
    def __init__(self):     # instance method to customize this class's object. to initialize the contents of this class Student() we use init method
        self.name = Name    # we are adding variables to objects
        self.dpt = Department


def main():
    student = get_student()
    exam = get_score()
    print(f"{student.name} is from {student.dpt}")
    print(f"{exam[1]} scored in {exam[0]}")

# Method 1: Without using the INIT method
# def get_student():
#     student = Student()  #created student object same as the class name
#     student.name = input("Name: ")
#     student.dpt = input("Department: ")  # name and dpt are attributes/instance variables of the Student class
#     return student
#            Method 2: when init is instantiated

def get_student():
    name = input("Name: ")
    dpt = input("Department: ")
    student = Student(name,dpt)  # treating name of the class "Student" as function and passing two values. This is called constructor call, constructing Student object for me 
    return student
# Same can be implemented by return as tuples
def get_score():

    subject = input("Subject Name: ")
    score = input("Add score: ")
    return (subject, score) # this tuple returns subject and score to the get_score() in main and store it to a single varibale exam

# we can also return a list i-e [subject, score] to the same function in main if we want to mutate the values of these variables o. tuple is fine

if __name__ == "__main__":
    main()





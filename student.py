def main():
    name, dpt = get_student()
    exam = get_score()
    print(f"{name} is from {dpt}")
    print(f"{exam[1]} scored in {exam[0]}")


def get_student():
    name = input("Name: ")
    dpt = input ("Department: ")
    return name, dpt

# Same can be implemented by return as tuples
def get_score():
    subject = input("Subject Name: ")
    score = input("Add score: ")
    return (subject, score) # this tuple returns subject and score to the get_score() in main and store it to a single varibale exam

# we can also return a list i-e [subject, score] to the same function in main if we want to mutate the values of these variables o. tuple is fine

if __name__ == "__main__":
    main()





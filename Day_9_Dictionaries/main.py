#declaring a dictionary
# programming_dictionary = {"bug": "A bug is a mistake or flaw in a program’s code that causes it to behave in an unintended way — like crashing, giving the wrong result, or acting unexpectedly.", 
                        #  "function": "A function is a reusable block of code that performs a specific task. You can call (run) a function whenever you need that task done, often with inputs (called parameters) and sometimes with an output (called a return value).",
                        #  "loop": "The action of doing something ove and over again."
                        #  }
#retrieving items from dictionary
# print(programming_dictionary["function"])

#adding items to a dictionary
# programming_dictionary["do-while"] = "This guarantees the code inside runs at least once — even if the condition is false on the first check"
# print(programming_dictionary)

#create an empty dictionary
# empty_dictionary = {}

#wipe a dictionary
#programming_dictionary = {}

#edit an item in dictionary
# programming_dictionary["do-while"] = "The loop body executes at least once, even if the condition is initially false."

# for key in programming_dictionary:
#     print(f"{key}: {programming_dictionary[key]}")


student_scores = {
        "harry": 91,
        "ron": 90,
        "hermine": 87,
        "draco": 79,
        "neville": 67
}

student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        print(student, " : ", student_scores[student], end="\n")
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectation"
        print(student, " : ", student_scores[student], end="\n")
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
        print(student, " : ", student_scores[student], end="\n")
    else:
        student_grades[student] = "Fail"
        print(student, " : ", student_scores[student], end="\n")

print("\n")

for key in student_grades:
    print(key, ": ", student_grades[key])
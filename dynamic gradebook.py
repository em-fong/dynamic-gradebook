"""
Dynamic tool for teachers to keep track of student grades and average class scores.


"""
#ask for number of students in class, makes sure its valid
students = int(input("How many students are in your class?: "))
while students < 1:
    print("Invalid number of students. Try again.")
    students = int(input("How many students are in your class?: "))

#asks for number of tests to grade, makes sure its valid
print()
tests = int(input("How many tests in this class?: "))
while tests < 1:
    print("Invalid number of tests. Try again.")
    tests = int(input("How many tests are in this class?: "))

#accumulator set up outside of outer loop
all_scores = 0

#outer for loop to count iterations through num of students
for i in range(1, students + 1):
    print()
    print("**** Student", i, "****")
    score_total = 0

    #inner for loop to iterate through num of tests
    for stu_scores in range(1, tests + 1):
        score = int(input("Enter score for test #" + str(stu_scores) + ": "))

        #make sure user enters valid test scores
        while score < 1:
            print("Invalid score. Try again.")
            score = int(input("Enter score for test #" + str(stu_scores) + ": "))

        #make sure calculations are only carried out on valid input
        if score >= 0:
            score_total += score
            avg_student = score_total/tests
    all_scores += (avg_student/students)

    #print average score per student with formatting
    print()
    print("Average score for student #" + str(i), "is", format(avg_student, ".2f"))

#print total average score with formatting
print()
print("Average score for all students is", format(all_scores, ".2f"))


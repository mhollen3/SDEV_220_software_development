## Matthew Hollen ##
## studentrecords.py ##
## This app will take a student's last name, first name, and their GPA and validate whether or not that student qualifies for the deans list or honor roll ##

while True:
    student_last = input(
        "Please enter the student's last name. You can exit this program by entering (ZZZ) ---").lower()
    if student_last != 'zzz':
        student_first = input(
            "Please enter the student's first name. ---")

        student_gpa = float(input(
            "Please enter the student's GPA. ---"))

        if student_gpa >= 3.5:
            print("Congratulations! You have made the Deans List!")

        elif student_gpa >= 3.25:
            print("Congratulations! You have made Honor Roll!")

        elif student_gpa < 3.25:
            print("Unforunately, this student did not make Deans List or Honor Roll.")

        else:
            print("Have a great day!")

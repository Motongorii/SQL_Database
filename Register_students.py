from main import Student


try:
    student_name = input("Enter Name\n")
    student_email = input("Enter email\n")
    student_password = input("Enter password\n")


    Student.create( stud_name=student_name, stud_email=student_email, stud_password=student_password)
    print("Student created successfully")
except:
    print("Failed to create student")
from main import Teacher


try:
    teacher_name = input("Enter Name\n")
    teacher_email = input("Enter email\n")
    teacher_password = input("Enter password\n")

    Teacher.create(Teach_name=teacher_name, Teach_email=teacher_email,Teach_password = teacher_password )
    print("Teacher created successfully")
except:
    print("Failed to create Teacher")
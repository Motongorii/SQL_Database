from main import Teacher


teachers = Teacher.select()
for teacher in teachers:
    print(teacher.Teach_name, teacher.Teach_email, teacher.Teach_password)
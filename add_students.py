students=[]
def add_students():
    id=int(input("Enter student id:"))
    name=input("Enter student name:")
    age=input("Enter student age:")
    course=input("Enter student course:")
    student={"id":id,"name":name,"age":age,"course":course}
    students.append(student)
    print("STUDENTS ADDED SUCCESFULLY....")

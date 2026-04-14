from add_students import students
def view_students():
    if len(students)==0:
        print("STUDENTS NOT FOUND....")
    else:
        for i in students:
            print(i)

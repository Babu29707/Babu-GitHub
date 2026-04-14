from add_students import students
def delete_students():
    name=input("Enter the Name for Delete:")
    for i in students:
        if i["name"]==name:
            students.remove(i)
            print("Students Deleted....")
            return
    print("Students Not Found....")


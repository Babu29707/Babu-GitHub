from add_students import students
def search_students():
    name=input("Enter Search Student Name:")
    found=False
    for i in students:
        if i["name"]==name:
            print("Student Found",i)
            found=True
    if not found:
        print("Student Not Found")





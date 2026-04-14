from add_students import students
from add_students import add_students
from view_students import view_students
from search_students import search_students
from delete_students import delete_students
while True:
    print("------STUDENT MANAGEMENT SYSTEM------")
    print("1.ADD STUDENT")
    print("2.VIEW STUDENT")
    print("3.SEARCH STUDENT")
    print("4.DELETE STUDENT")
    print("5.EXIT")
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        add_students()
    elif choice==2:
        view_students()
    elif choice==3:
        search_students()
    elif choice==4:
        delete_students()
    elif choice==5:
        print("EXIT")
        break
    else:
        print("INVALID CHOICE")

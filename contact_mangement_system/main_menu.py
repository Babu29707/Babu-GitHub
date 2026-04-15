
from add_contacts import add_contacts
from  view_all_contacts import view_all_contacts
from search_contacts import search_contacts
from delete_contacts import delete_contacts
while True:
    print("------CONTACT MANAGEMENT SYSTEM------")
    print("1.ADD CONTACT")
    print("2.VIEW CONTACT")
    print("3.SEARCH CONTACT")
    print("4.DELETE CONTACT")
    print("5.EXIT")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        add_contacts()
    elif choice == 2:
        view_all_contacts()
    elif choice == 3:
        search_contacts()
    elif choice == 4:
        delete_contacts()
    elif choice == 5:
        print("EXIT")
        break
    else:
        print("INVALID CHOICE")

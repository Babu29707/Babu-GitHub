from add_contacts import contacts

def search_contacts():
    contact_number = int(input("Enter Your Required Number: "))
    found = False
    for i in contacts:
        if i["contact_number"] == contact_number:
            print("Contact Number Found", i)
            found = True
    if not found:
        print("Contact Not Found")



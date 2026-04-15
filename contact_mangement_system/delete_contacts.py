from add_contacts import contacts
def delete_contacts():
    contact_numbers=int(input("Enter the number of contacts you want to delete: "))
    for i in contacts:
        if i["contact_number"]==contact_numbers:
            contacts.remove(i)
            print("Contact Deleted....")
            return
    print("Contact Not Found....")

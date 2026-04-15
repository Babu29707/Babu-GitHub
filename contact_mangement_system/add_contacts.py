contacts = []
def add_contacts():
    for i in range(5):  # allow 5 contacts
        contact_num = int(input("Enter the contact number: "))
        contact = {"contact_number": contact_num}  # fixed name
        contacts.append(contact)
        print("CONTACT ADDED SUCCESSFULLY")
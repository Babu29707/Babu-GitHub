from add_contacts import contacts
def view_all_contacts():
    if len(contacts)==0:
        print("CONTACTS NOT FOUND")
    else:
        for i in contacts:
            print("\n",i)



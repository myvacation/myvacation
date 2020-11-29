# making a simple contact book that allows users to add, update, delete, and print contacts

print ("Welcome to your contact book, we can add, delete, update and print your contacts!")
print ("The format of the contact book is contact name followed by phone number.")
name = input("Please enter your name  ")

contact_book = {}

def contact_changes(action):
    if action == "A":
        contact_name = input("Enter the contact name:  ")
        contact_numb = input("Please enter contact number:  ")
        contact_book[contact_name] = contact_numb

    elif action == "D":
        contact_delete = input("Please enter the name of the person you want to delete:  ")
        if contact_delete in contact_book.keys():
            del contact_book[contact_delete]
        else:
            print ("Contact not in dictionary")

    elif action == "U":
        contact_update= input("Please type the name of contact you want to update:  ")
        updated_phone= input("Please type the new phone number you want to insert:  ")
        contact_book[contact_update]= updated_phone

    elif action == "P":
        print (contact_book)

    return contact_book

action = True
while action != "E":
    action = input("What would you like to do? Type A for add, D for delete, U for update, P for print, or E for exit   ")
    contact_changes(action)
print ("Thanks for using")



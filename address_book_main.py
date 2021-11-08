from contact import Contact

address_book = []


def edit_contact(new_detail, updated_contact):
    """ method to edit contact detail using phone number"""
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.phone == new_detail:
            address_book[i] = updated_contact


def delete_contact(contact_to_delete):
    """ method to delete contact using first name"""
    for i in range(len(address_book)):
        contact = address_book[i]
        if contact.first_name == contact_to_delete:
            address_book.remove(contact)


def print_address_book():
    """ method to print address book list"""
    for i in range(len(address_book)):
        contact = address_book[i]
        print(contact)


contact_person = Contact("akash", "singh", "hsr", "bangalore", "karnataka", "221002", "8090433565", "abc@gmail.com")
address_book.append(contact_person)
print_address_book()

contact_to_edit = "8090433565"
updated_contact_person = Contact("akash", "singh", "hsr", "bangalore", "karnataka", "221002", "8090433565", "xyz"
                                                                                                            "@gmail.com")
edit_contact(contact_to_edit, updated_contact_person)
print_address_book()

contact_to_delete = "akash"
delete_contact(contact_to_delete)
print_address_book()
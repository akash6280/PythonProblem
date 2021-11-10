from contact import Contact
import json


class AddressBook:
    """class that manages operations on addressbook"""

    def __init__(self):
        self.address_book = []
        self.read_data_from_json_file()

    def add_contact(self, contact):
        """method to add contact to list """
        self.address_book.append(contact)
        self.write_data_to_json_file()

    def edit_contact(self, new_detail, updated_contact):
        """ method to edit contact detail using phone number"""
        print(len(self.address_book))
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.phone == new_detail:
                self.address_book[i] = updated_contact
        self.write_data_to_json_file()

    def delete_contact(self, contact_to_delete):
        """ method to delete contact using first name"""
        for each_a in self.address_book:
            contact = each_a
            if contact.first_name == contact_to_delete:
                self.address_book.remove(contact)
        self.write_data_to_json_file()

    def search_person_by_state(self, state):
        """ method to search person by state in address book"""
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.state == state:
                print(contact)

    def search_person_by_city(self, city):
        """ method to search person by city in address book"""
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            if contact.city == city:
                print(contact)

    def write_data_to_json_file(self):
        """ method to write data to json file"""
        address_books = []
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            address_books.append(contact.json_object())
        with open("address.json", 'w') as output_file:
            json.dump(address_books, output_file)

    def read_data_from_json_file(self):
        """method to read data from json file"""
        with open("address.json") as json_file:
            data = json.load(json_file)
        for contact in data:
            first_name = contact["first_name"]
            last_name = contact["last_name"]
            address = contact["address"]
            city = contact["city"]
            state = contact["state"]
            zip_code = contact["zip_code"]
            phone = contact["phone"]
            email = contact["email"]
            self.address_book.append(Contact(first_name, last_name, address, city
                                             , state, zip_code, phone, email))

    def print_address_book(self):
        """ method to print address book list"""
        for i in range(len(self.address_book)):
            contact = self.address_book[i]
            print(contact)


if __name__ == "__main__":
    address_book_object = AddressBook()
    while True:
        print(" 1 for add contact \n 2 for edit contact \n 3 for delete contact \n 4 search person by city \n 5 search "
              "person by state \n 6 map city with person \n 7 map state with person \n 8 to exit")
        option = int(input("enter choice "))
        if option == 1:
            first_name = input("enter first name \n")
            last_name = input("enter last name \n ")
            address = input("enter address \n")
            city = input("enter city \n ")
            state = input("enter state \n ")
            zip_code = input("enter zip code \n")
            phone = input("enter phone number \n")
            email = input("enter email \n")
            address_book_object.add_contact(
                Contact(first_name, last_name, address, city, state, zip_code, phone, email))
            address_book_object.print_address_book()

        elif option == 2:
            phone = input("enter phone number \n")
            first_name = input("enter first name \n")
            last_name = input("enter last name \n")
            address = input("enter address \n")
            city = input("enter city \n")
            state = input("enter state \n")
            zip_code = input("enter zip code \n")
            email = input("enter email \n")
            updated_contact_person = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
            address_book_object.edit_contact(phone, updated_contact_person)
            address_book_object.print_address_book()

        elif option == 3:
            name = input("enter contact name \n ")
            address_book_object.delete_contact(name)
            address_book_object.print_address_book()

        elif option == 4:
            city = input("enter city name \n")
            address_book_object.search_person_by_city(city)

        elif option == 5:
            state = input("enter state name \n")
            address_book_object.search_person_by_state(state)

        elif option == 6:
            address_book_object.map_city_with_person()

        elif option == 7:
            address_book_object.map_state_with_person()

        else:
            exit()

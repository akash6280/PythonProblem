from address_book_exception import AddressBookException


class Contact:
    """ class that represent person details """

    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    @property
    def first_name(self):
        return self._first_name

    # a setter function
    @first_name.setter
    def first_name(self, first_name):
        if first_name is None or first_name.strip() == "":
            raise AddressBookException('Invalid first name')
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    # a setter function
    @last_name.setter
    def last_name(self, last_name):
        if not last_name or last_name.strip() == "":
            raise AddressBookException('Invalid last name')
        self._last_name = last_name

    @property
    def address(self):
        return self._address

    # a setter function
    @address.setter
    def address(self, address):
        if not address or address.strip() == "":
            raise AddressBookException('Invalid Address')
        self._address = address

    @property
    def city(self):
        return self._city

    # a setter function
    @city.setter
    def city(self, city):
        if not city or city.strip() == "":
            raise AddressBookException('Invalid city')
        self._city = city

    # a getter function
    @property
    def state(self):
        return self._state

    # a setter function
    @state.setter
    def state(self, state):
        if not state or state.strip() == "":
            raise AddressBookException('Invalid state')
        self._state = state

    @property
    def zip_code(self):
        return self._zip_code

    # a setter function
    @zip_code.setter
    def zip_code(self, zip_code):
        if not zip_code or zip_code.strip() == "":
            raise AddressBookException('Invalid zip code')
        self._zip_code = zip_code

    @property
    def phone(self):
        return self._phone

    # a setter function
    @phone.setter
    def phone(self, phone):
        if not phone or phone.strip() == "":
            raise AddressBookException('Invalid phone')
        self._phone = phone

    @property
    def email(self):
        return self._email

    # a setter function
    @email.setter
    def email(self, email):
        if not email or email.strip() == "":
            raise AddressBookException('Invalid email')
        self._email = email

    def __str__(self):
        return "first_name: " + self.first_name + "\nlast_name: " + self.last_name + "\naddress: " + self.address \
               + "\ncity: " + self.city + "\nstate: " + self.state + "\nzip_code: " + self.zip_code + "\nphone: " \
               + self.phone + "\nemail: " + self.email

    def json_object(self):
        """ method that return json object"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone": self.phone,
            "email": self.email
        }

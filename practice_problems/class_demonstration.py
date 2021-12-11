class PersonDetail:
    """ Class that represent user detail"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        """ return first name"""
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """ function to set first name"""
        self._first_name = value

    @property
    def last_name(self):
        """ return last name"""
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ function to set last name"""
        self._last_name = value

    def __str__(self):
        return self.first_name + " " + self.last_name


person1 = PersonDetail("Akash", "Singh")
print(person1)
print(PersonDetail.first_name.__doc__)

# program to illustrate public access modifier in a class
class Geek:

    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def display_age(self):
        # accessing public data member
        print("Age: ", self.geekAge)


# creating object of the class
obj = Geek("R2J", 20)

# accessing public data member
print("Name: ", obj.geekName)

# calling public member function of the class
obj.display_age()
print(obj.geekName)

class user:

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def _userdetails(self):
        print("Id: {}, Name: {}".format(self._id, self._name))


class Employees(user):
    pass


e1 = Employees(1, "Suresh")
print(e1._id)
print(e1._name)
e1._userdetails()


class user:
    __id = 10
    __name = "Suresh"

    def __userdetails(self):
        print("Private Method")


u1 = user()
u1._user__id = 11
user.__id = 12
print(user.__id)
print(u1._user__id)

print(u1.__id)
print(u1.__name)
u1.__userdetails()

class Person:
    def __init__(self, name, age, height):
        self.name = name  # public
        self._age = age  # protected
        self.__height = height  # private


p1 = Person("John", 20, 170)

print(p1.name)  # public: can be accessed
print(p1._age)  # protected: can be accessed but not advised
# print(p1.__height)  # private: will give AttributeError
# print(Person.__height)
print(p1._Person__height)

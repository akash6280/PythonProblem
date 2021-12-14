import pytest

from address_book_exception import AddressBookException
from contact import Contact
from address_book_main import AddressBook


@pytest.fixture()
def address_book():
    """
        function to create contact object and add it  to addressbook
        :return: oject
    """
    contact_person = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "9740142826",
                             "agam@gmail.com")
    address_book = AddressBook()
    address_book.add_contact(contact_person)
    return address_book


def test_add_contact_with_correct_details(address_book):
    """
       to test add contact with correct input
       :param - address_book:
       :return: None
    """
    assert len(address_book.address_book) == 1


def test_edit_contact_that_exist(address_book):
    """
           to test edit contact with contact that exist
           :param - address_book:
           :return: None
    """
    unique_detail = "9740142826"
    contact_to_update = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "9740142826",
                                "xyz@gmail.com")
    contact = address_book.edit_contact(unique_detail, contact_to_update)
    assert contact.phone == contact_to_update.phone


def test_delete_contact_with_correct_count(address_book):
    """
      to test delete contact with contact that exist
      :param - address_book:
      :return: None
    """
    contact_to_delete = "agam"
    address_book.delete_contact(contact_to_delete)
    assert len(address_book.address_book) == 0


def test_search_person_by_city_with_correct_city(address_book):
    """
         to test search person by city with city that exist
         :param - address_book:
         :return: None
    """
    city_to_be_searched = "varanasi"
    result = address_book.search_person_by_city(city_to_be_searched)
    assert result == True


def test_search_person_by_state_with_correct_state(address_book):
    """
        to test search person by state with state that exist
        :param - address_book:
        :return: None
    """
    state_to_be_searched = "uttar pradesh"
    result = address_book.search_person_by_state(state_to_be_searched)
    assert result == True


def test_map_state_with_person_with_existing_state(address_book):
    state_map = address_book.map_state_with_person()
    assert len(state_map["uttar pradesh"]) == 1


def test_map_city_with_person_with_existing_city(address_book):
    city_map = address_book.map_city_with_person()
    assert len(city_map["varanasi"]) == 1


@pytest.mark.xfail(raises=AddressBookException)
def test_add_contact_given_empty_first_name():
    """
    to test add contact with empty first name
    :return:
    """
    contact1 = Contact("", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "123456789",
                       "abc@gmail.com")


@pytest.mark.xfail(raises=AddressBookException)
def test_add_contact_given_none_first_name():
    """
    to test add contact with invalid first name
    :return:
    """
    contact1 = Contact(None, "singh", "cantt", "varanasi", "uttar pradesh", "221002", "123456789",
                       "abc@gmail.com")


@pytest.mark.xfail(raises=AddressBookException)
def test_add_contact_given_city_as_empty():
    """
    to test add contact with empty first name
    :return:
    """
    contact1 = Contact("akash", "singh", "cantt", "", "uttar pradesh", "221002", "123456789",
                       "abc@gmail.com")


@pytest.mark.xfail(raises=AddressBookException)
def test_add_contact_given_city_as_none():
    """
    to test add contact with invalid first name
    :return:
    """
    contact1 = Contact("akash", "singh", "cantt", None, "uttar pradesh", "221002", "123456789",
                       "abc@gmail.com")


@pytest.mark.xfail
def test_edit_contact_that_doesnot_exist(address_book):
    """
        to test edit contact with contact that  does not exist
        :param - address_book:
        :return: None
    """
    unique_detail = "123456789"
    contact_to_update = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "123456789",
                                "abc@gmail.com")
    contact = address_book.edit_contact(unique_detail, contact_to_update)
    assert contact.phone == contact_to_update.phone


@pytest.mark.xfail
def test_delete_contact_with_contact_not_exist(address_book):
    """
        to test delete contact with contact that exist
        :param - address_book:
        :return: None
    """
    contact_to_delete = "adam"
    address_book.delete_contact(contact_to_delete)
    assert len(address_book.address_book) == 0


@pytest.mark.xfail
def test_search_person_by_city_with_incorrect_city(address_book):
    """
       to test search person by city with city  that does not exist
       :param - address_book:
       :return: None
    """
    city_to_be_searched = "chennai"
    result = address_book.search_person_by_city(city_to_be_searched)
    assert result == True


@pytest.mark.xfail
def test_search_person_by_state_with_incorrect_state(address_book):
    """
      to test search person by state with state  that does not exist
      :param - address_book:
      :return: None
     """
    state_to_be_searched = "karnataka"
    result = address_book.search_person_by_state(state_to_be_searched)
    assert result == True


@pytest.mark.xfail
def test_map_state_with_person_with_state_not_existing(address_book):
    state_map = address_book.map_state_with_person()
    assert len(state_map["MP"]) == 1


@pytest.mark.xfail
def test_map_city_with_person_with_city_not_existing(address_book):
    city_map = address_book.map_city_with_person()
    assert len(city_map["bhopal"]) == 1

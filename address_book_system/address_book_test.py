import pytest
from contact import Contact
from address_book_main import AddressBook


@pytest.fixture()
def address_book():
    contact_person = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "9740142826",
                             "agam@gmail.com")
    address_book = AddressBook()
    address_book.add_contact(contact_person)
    return address_book


def test_add_contact(address_book):
    assert len(address_book.address_book) == 1


def test_edit_contact(address_book):
    new_detail = "xyz@gmail.com"
    contact_to_update = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "9740142826",
                                "agam@gmail.com")
    address_book.edit_contact(new_detail, contact_to_update)
    assert len(address_book.address_book) == 1


def test_delete_contact(address_book):
    contact_to_delete = "agam"
    address_book.delete_contact(contact_to_delete)
    assert len(address_book.address_book) == 0


def test_search_person_by_city(address_book):
    city_to_be_searched = "varanasi"
    address_book.search_person_by_city(city_to_be_searched)
    assert len(address_book.address_book) == 1


def test_search_person_by_state(address_book):
    state_to_be_searched = "uttar pradesh"
    address_book.search_person_by_state(state_to_be_searched)
    assert len(address_book.address_book) == 1


def test_map_state_with_person(address_book):
    state_map = address_book.map_state_with_person()
    assert len(state_map["uttar pradesh"]) == 1


def test_map_city_with_person(address_book):
    city_map = address_book.map_city_with_person()
    assert len(city_map["varanasi"]) == 1

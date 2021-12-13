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


def test_add_contact_with_correct_count(address_book):
    assert len(address_book.address_book) == 1


def test_edit_contact_that_exist(address_book):
    unique_detail = "9740142826"
    contact_to_update = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "9740142826",
                                "xyz@gmail.com")
    contact = address_book.edit_contact(unique_detail, contact_to_update)
    assert contact.phone == contact_to_update.phone


def test_delete_contact_with_correct_count(address_book):
    contact_to_delete = "agam"
    address_book.delete_contact(contact_to_delete)
    assert len(address_book.address_book) == 0


def test_search_person_by_city_with_correct_city(address_book):
    city_to_be_searched = "varanasi"
    result = address_book.search_person_by_city(city_to_be_searched)
    assert result == True


def test_search_person_by_state_with_correct_state(address_book):
    state_to_be_searched = "uttar pradesh"
    result = address_book.search_person_by_state(state_to_be_searched)
    assert result == True


def test_map_state_with_person_with_existing_state(address_book):
    state_map = address_book.map_state_with_person()
    assert len(state_map["uttar pradesh"]) == 1


def test_map_city_with_person_with_existing_city(address_book):
    city_map = address_book.map_city_with_person()
    assert len(city_map["varanasi"]) == 1


@pytest.mark.xfail
def test_add_contact_return_incorrect_count(address_book):
    assert len(address_book.address_book) == 0


@pytest.mark.xfail
def test_edit_contact_that_doesnot_exist(address_book):
    unique_detail = "123456789"
    contact_to_update = Contact("agam", "singh", "cantt", "varanasi", "uttar pradesh", "221002", "123456789",
                                "abc@gmail.com")
    contact = address_book.edit_contact(unique_detail, contact_to_update)
    assert contact.phone == contact_to_update.phone


@pytest.mark.xfail
def test_delete_contact_with_incorrect_count(address_book):
    contact_to_delete = "adam"
    address_book.delete_contact(contact_to_delete)
    assert len(address_book.address_book) == 0


@pytest.mark.xfail
def test_search_person_by_city_with_incorrect_city(address_book):
    city_to_be_searched = "chennai"
    result = address_book.search_person_by_city(city_to_be_searched)
    assert result == True


@pytest.mark.xfail
def test_search_person_by_state_with_incorrect_state(address_book):
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

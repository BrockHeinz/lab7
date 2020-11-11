# Functions to make:
# new_contact_store
# add_new_contact
# remove_contact
# has_contact
# get_contact_string
# update_contact_first_name
# update_contact_last_name
# update_contact_email
# update_contact_phone_number
# update_contact_birthday
def new_contact_store():
    contacts = {}
    return contacts


def add_new_contact(contacts, first_name, last_name, email, phone_number, birthday):
    contacts[first_name + last_name] = [first_name, last_name, email, phone_number, birthday]
    return contacts


def remove_contact(contacts, first_name, last_name):
    contacts.pop(first_name + last_name)
    return contacts


def has_contact(contacts, first_name, last_name):
    if first_name + last_name in contacts:
        return True
    else:
        return False


def get_contact_string(contacts, first_name, last_name):
    entry = contacts.get(first_name + last_name)
    return str(entry)


def update_contact_first_name(contacts, first_name, last_name, new_field_value):
    # creates a new dictionary entry with the same contents, but with an
    # updated key to accomodate the new first name; removes the old one
    contacts[new_field_value + last_name] = contacts.get(first_name + last_name)
    contacts.get(new_field_value + last_name)[0] = new_field_value
    contacts.pop(first_name + last_name)
    return contacts


def update_contact_last_name(contacts, first_name, last_name, new_field_value):
    # creates a new dictionary entry with the same contents, but with an
    # updated key to accomodate the new last name; removes the old one
    contacts[first_name + new_field_value] = contacts.get(first_name + last_name)
    contacts.get(first_name + new_field_value)[1] = new_field_value
    contacts.pop(first_name + last_name)
    return contacts


def update_contact_email(contacts, first_name, last_name, new_field_value):
    contacts.get(first_name + last_name)[2] = new_field_value
    return contacts


def update_contact_phone_number(contacts, first_name, last_name, new_field_value):
    contacts.get(first_name + last_name)[3] = new_field_value
    return contacts


def update_contact_birthday(contacts, first_name, last_name, new_field_value):
    contacts.get(first_name + last_name)[4] = new_field_value
    return contacts

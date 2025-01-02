from collections import UserList
from name import Name
from phone import Phone
from inputerror import input_error

class Record(UserList):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    @input_error
    def add_phone(self, phone):
        if not phone:
            raise ValueError("Please provide a phone number.")
        self.phones.append(Phone(phone))
        return f"Phone {phone} added for contact {self.name}."

    @input_error
    def change_contact_phone(self, old_phone, new_phone):
        if not old_phone or not new_phone:
            raise ValueError("Please provide both an old phone and a new phone number.")
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                break
        self.phones.append(Phone(new_phone))
        return f"Phone number {old_phone} changed to {new_phone} for contact {self.name}."

    @input_error
    def delete_contact_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                break
        return f"Phone number {old_phone} deleted for contact {self.name}."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
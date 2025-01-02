from collections import UserDict
import inputerror

class AddressBook(UserDict):
        
    def list_contacts(contacts):
        return "Contacts:\n" + "\n".join(f"{name[0].upper() + name[1:]}: {phone}" for name, phone in contacts.items())

    @inputerror
    def search_contact(args, contacts):
        if len(args) != 1:
            raise ValueError("Please provide a name.")
        name = args[0].casefold()
        if name in contacts:
            return f"Contact found: {name[0].upper() + name[1:]}: {contacts[name]}"
        else:
            raise KeyError("Contact not found.")
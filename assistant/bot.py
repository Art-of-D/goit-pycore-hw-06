def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)
    return inner

def load_contacts(contacts):
    try:
        with open("./assistant/phonebook.txt", "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name] = phone
    except FileNotFoundError:
        print("No contacts found. Please add new contact.")

def record_contacts(contacts):
  with open("./assistant/phonebook.txt", "w") as file:
    try :
        print("Saving contacts...")
        if len(contacts) == 0:
            print("No contacts to save.")
            return
        records = "\n".join(f"{name}, {phone}" for name, phone in contacts.items())
        file.write(records)
    except Exception as e:
        print(f"Error saving contacts: {e}")
    finally:
        contacts = {}

def parse_input(user_input):
    if not user_input:
        print("Please enter a command.")
        return "commands", []
    else: 
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide a name and phone number.")
    name, phone = args
    contacts[name.casefold()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide a name and a new phone number.")
    name, phone = args
    contacts[name.casefold()] = phone
    return "Contact changed."

@input_error
def delete_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Please provide a name.")
    name = args[0].casefold()
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else:
        raise KeyError("Contact not found.")
    
def list_contacts(contacts):
    return "Contacts:\n" + "\n".join(f"{name[0].upper() + name[1:]}: {phone}" for name, phone in contacts.items())

@input_error
def search_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Please provide a name.")
    name = args[0].casefold()
    if name in contacts:
        return f"Contact found: {name[0].upper() + name[1:]}: {contacts[name]}"
    else:
        raise KeyError("Contact not found.")
    


def main():
    """
    Runs the assistant bot.

    This function is the entry point of the program. It will
    load all the existing contacts from a file, and then
    enter an infinite loop, where it will wait for user
    input and act accordingly.

    The available commands are:

    - hello: prints a greeting message
    - add <name> <phone>: adds a new contact to the phonebook
    - change <name> <phone>: changes the phone number of an existing contact
    - delete <name>: deletes an existing contact
    - all: prints all the contacts in the phonebook
    - phone <name>: prints the phone number of the contact with the given name
    - commands: prints a list of all the available commands
    - close, exit: saves the current state of the phonebook and exits the program

    If the user enters an invalid command, the bot will print
    an error message and then wait for the next command.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    load_contacts(contacts)
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            record_contacts(contacts)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "phone":
            print(search_contact(args, contacts))
        elif command == "commands":
            print("Available commands: hello, add, change, delete, all, phone, close, exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()


# from collections import UserDict

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     # реалізація класу
# 		pass

# class Phone(Field):
#     # реалізація класу
# 		pass

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []

#     # реалізація класу

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     # реалізація класу
# 		pass
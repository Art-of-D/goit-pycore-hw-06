from internal.addressbook import AddressBook
from internal.record import Record

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

book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

john_record.delete_contact_phone("5555555555")
print(1, john_record)

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
print("Всі записи у книзі:")
for name, record in book.data.items():
    print(record)

# Знаходження телефону для John
john = book.find("John")
print("Found:", john)
# Редагування телефону для John
book.edit_phone("John", "1234567890", "5555555555")
print("After editing:",john)  # Виведення: Contact name: John, phones: 5555555555

# Пошук конкретного телефону у записі John
found_phone = book.find_phone("5555555555")
print(f"Found phone: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
print("Всі записи у книзі:")
for name, record in book.data.items():
    print(record)
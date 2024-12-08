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
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.casefold()] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name.casefold()] = phone
    return "Contact changed."

def delete_contact(args, contacts):
    name = args[0].casefold()
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else:
        return "Contact not found."

def list_contacts(contacts):
    return "Contacts:\n" + "\n".join(f"{name[0].upper() + name[1:]}: {phone}" for name, phone in contacts.items())

def search_contact(args, contacts):
    name = args[0].casefold()
    if name in contacts:
        return f"Contact found: {name[0].upper() + name[1:]}: {contacts[name]}"
    else:
        return "Contact not found."
    


def main():
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
            if len(args) != 2:
                print("Please provide a name and phone number.")
                continue
            print(add_contact(args, contacts))
        elif command == "change":
            if len(args) != 2:
                print("Please provide a name and a new phone number.")
                continue
            print(change_contact(args, contacts))
        elif command == "delete":
            if len(args) != 1:
                print("Please provide a name.")
                continue
            print(delete_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "phone":
            if len(args) != 1:
                print("Please provide a name.")
                continue
            print(search_contact(args, contacts))
        elif command == "commands":
            print("Available commands: hello, add, change, delete, all, phone, close, exit")
        else:
            print("Invalid command. If you need help, type 'commands'.")

if __name__ == "__main__":
    main()

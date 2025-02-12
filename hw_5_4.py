def input_error(func):
    """Decorator to handle input errors and exceptions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner


def parse_input(user_input):
    """Parses the entered command and its arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    """Adds a new contact."""
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """Changes the phone number for an existing contact."""
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    """Displays the phone number for the specified contact."""
    name = args[0]
    if name in contacts:
        return f"The phone number for {name} is {contacts[name]}."


@input_error
def show_all(contacts):
    """Displays all saved contacts and their numbers."""
    if not contacts:
        return "No contacts saved."
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

import pickle
from addressbook import AddressBook, Record, Name, Phone, Birthday


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()


def main():
    book = load_data()
    print("Welcome to the Assistant Bot! Type 'help' to see available commands.")

    while True:
        user_input = input(">>> ").strip()
        if not user_input:
            continue

        command, *args = user_input.split()

        if command in ("exit", "close", "goodbye"):
            save_data(book)
            print("Good bye!")
            break

        elif command == "add":
            if len(args) < 2:
                print("Usage: add [name] [phone] [birthday YYYY-MM-DD optional]")
                continue
            name = Name(args[0])
            phone = Phone(args[1])
            birthday = Birthday(args[2]) if len(args) > 2 else None
            record = Record(name, phone, birthday)
            book.add_record(record)
            print("Contact added!")

        elif command == "change":
            if len(args) != 3:
                print("Usage: change [name] [old_phone] [new_phone]")
                continue
            record = book.find(args[0])
            if not record:
                print("Contact not found.")
                continue
            record.edit_phone(Phone(args[1]), Phone(args[2]))
            print("Phone changed.")

        elif command == "phone":
            if len(args) != 1:
                print("Usage: phone [name]")
                continue
            record = book.find(args[0])
            if record:
                print(record)
            else:
                print("Contact not found.")

        elif command == "show":
            if not book.data:
                print("Address book is empty.")
            else:
                for record in book.data.values():
                    print(record)

        elif command == "delete":
            if len(args) != 1:
                print("Usage: delete [name]")
                continue
            book.delete(args[0])
            print("Contact deleted.")

        elif command == "help":
            print("Commands:")
            print(" add [name] [phone] [birthday YYYY-MM-DD optional]")
            print(" change [name] [old_phone] [new_phone]")
            print(" phone [name]")
            print(" show - show all contacts")
            print(" delete [name]")
            print(" exit/close/goodbye - exit the program")

        else:
            print("Unknown command. Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()

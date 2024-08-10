from method import *

def main():
    book = AddressBook.load_from_file()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        input_text = user_input.split()
        command = input_text[0].lower()
        args = input_text[1:]

        if command in ["close", "exit"]:
            book.save_to_file()
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
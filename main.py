from module01 import *

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            return f"Проблема з контактами {str(e)}"

    return wrapper

@input_error
def add_contact(args, book: AddressBook):
    if len(args) < 2:
        return "Не вірний формат вводу. Застосувати: add -name- -number-"
    
    name, phone, *_ = args # Ігноруємо додаткові аргументи
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    try:
        record.add_phone(phone)
    except ValueError as e:
        return str(e)
    return message

@input_error
def change_contact(args, book: AddressBook):
    if len(args) < 3:
        return "Не вірний формат вводу. Застосувати: change -name- -old_number- -new_number-"

    name, old_phone, new_phone = args
    record = book.find(name)

    if record:
        record.edit_phone(old_phone, new_phone)
        return "Контакти оновлено"

    return "Контакти не знайдено"

@input_error
def show_phone(args, book: AddressBook):
    if len(args) < 1:
        return "Не вірний формат вводу. Застосувати: phone -name-"

    name, *_ = args
    record = book.find(name)
    if record:
        return f"Номери користувача {name}:{', '.join(phone.value for phone in record.phones)}"

    return "Контакти не знайдено"

def show_all_contacts(book: AddressBook):
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Не вірний формат вводу. Застосувати: add-birthday -name- -DD.MM.YYYY-"

    name, birthday, *_ = args

    try:
        birthday = datetime.strptime(birthday, "%d.%m.%Y").date()
    except ValueError:
        return "Такої дати не існує"
    
    record = book.find(name)
    if record:
        try:
            record.add_birthday(birthday.strftime("%d.%m.%Y"))
        except ValueError as e:
            return str(e)

        return "День народження додано"

    return "Контакт не знайдено"

@input_error
def show_birthday(args, book: AddressBook):
    if len(args) < 1:
        return "Не вірний формат вводу. Застосувати: show-birthday -name-"

    name, *_ = args
    record = book.find(name)

    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday}"

    return "День народження не вказано або контакт не знайдено"

@input_error
def birthdays(book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()

    if not upcoming_birthdays:
        return "Немає днів народжень протягом наступного тижня"

    return "\n".join(str(record) for record in upcoming_birthdays)

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        input_text = user_input.split()
        command = input_text[0].lower()
        args = input_text[1:]

        if command in ["close", "exit"]:
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
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
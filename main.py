from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def validate(self):
        # Логіка валідації для імені
        if not self.value:
            raise ValueError("Name is required.")


class Phone(Field):
    def validate(self):
        # Логіка валідації для номера телефону (10 цифр)
        if self.value and not self.value.isdigit() or len(self.value) != 10:
            raise ValueError("Invalid phone number format.")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_field = Phone(phone)
        phone_field.validate()
        self.phones.append(phone_field)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]


class AddressBook(UserDict):
    def add_record(self, record):
        if not isinstance(record, Record):
            raise ValueError("Invalid record type.")
        record.name.validate()
        self.data[record.name.value] = record

    def remove_record(self, name):
        del self.data[name]

    def search_records(self, query):
        # Логіка пошуку за записами
        return [record for record in self.data.values() if query.lower() in record.name.value.lower()]


# Приклад використання:
if __name__ == "__main__":
    address_book = AddressBook()

    # Додавання запису
    contact1 = Record("John Doe")
    contact1.add_phone("1234567890")
    address_book.add_record(contact1)

    # Пошук запису
    results = address_book.search_records("John")
    for result in results:
        print(result.name.value, [phone.value for phone in result.phones])

    # Видалення запису
    address_book.remove_record("John Doe")

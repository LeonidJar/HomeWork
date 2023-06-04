phone_book: list[dict[str, str]] = []
path = 'phone.txt'

def open_phonebook():
    global phone_book, path

    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()

    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})


def save_phonebook():
    global phone_book, path
    data = []

    for contact in phone_book:
        contact = ':'.join([value for value in contact.values()])
        data.append(contact)

    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(data))


def get_phonebook() -> list[dict[str, str]]:
    global phone_book
    return phone_book


def add_contact(contact: dict[str, str]):
    global phone_book
    phone_book.append(contact)
    return contact.get('name')


def find_contact(name: str) -> dict[str, str]:
    global phone_book
    find_result = []

    for contact in phone_book:
        if contact.get('name') == name:
            find_result.append(contact)

    return find_result


def change_contact(new_contact: dict[str, str], index: int):
    global phone_book

    for i in range(len(phone_book)):
        if i == index - 1:
            phone_book[i] = new_contact 


def del_contact(index: int):
    return phone_book.pop(index - 1).get('name')
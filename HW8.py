# 1 Открыть файл +
# 2 Сохранить файл
# 3 Показать телефонную книгу +
# 4 Добавить контакт +
# 5 Найти контакт +
# 6 Изменить контакт +
# 7 Удалить контакт +
# 8 Выход +

def init_menu():
    path = 'phonebook.txt'

    menu = {1: 'open file',
            2: 'save file',
            3: 'show contacts',
            4: 'add contact',
            5: 'find contact',
            6: 'change contact',
            7: 'delete contact',
            8: 'exit'}
    
    menu_search = {1: 'search by name',
                   2: 'search by middle name',
                   3: 'search by last name',
                   4: 'search by phone number'}

    print('\n'.join("{}: {}".format(k, v) for k, v in menu.items()))

    n = int(input())
    print()

    if n == 1:
        path = create_open_file()
    elif n == 3:
        read_file(path)
    elif n == 4:
        add_into_file(path)
    elif n == 5:
        print('\n'.join("{}: {}".format(k, v) for k, v in menu_search.items()))
        n_1 = int(input())
        print()
        if n_1 == 1:
            find_contact_by_name_file(path)
        elif n_1 == 2:
            find_contact_by_midname_file(path)
        elif n_1 == 3:
            find_contact_by_lastname_file(path)
        elif n_1 == 4:
            find_contact_by_number_file(path)
    elif n == 6:
        change_contact_file(path)
    elif n == 7:
        delete_contact_file(path)
    elif n == 8:
        quit()

    

def create_open_file():
    path = input('Enter file name ').lower()
    data = open(path, 'a', encoding='UTF-8')

    data.close()
    init_menu()
    return path

def add_into_file(path):
    data = open(path, 'a', encoding='UTF-8')
    data.write(input('Enter name ').capitalize() + ' ')
    data.write(input('Enter middle name ').capitalize() + ' ')
    data.write(input('Enter last name ').capitalize() + ' ')
    phone = input('Enter phone number ')
    data.write(f'{phone}\n')

    data.close()
    init_menu()

def read_file(path):
    data = open(path, 'r', encoding='UTF-8')
    print(data.read())

    data.close()
    init_menu()

def find_contact_by_name_file(path):
    data = open(path, 'r', encoding='UTF-8')
    name = input('Enter name ').capitalize()
    count = 0

    for line in data.readlines():
        if name in line:
            print(line[:len(line)-1])
            count += 1
    # Не понимаю почему не работает !      
    # print(line[:len(line)-1] if name in line else "not found" for line in data.readlines())

    if count == 0:
        print('contact not found')
    
    data.close()
    print()
    init_menu()

def find_contact_by_midname_file(path):
    data = open(path, 'r', encoding='UTF-8')
    mid_name = input('Enter middle name ').capitalize()
    count = 0

    for line in data.readlines():
        if mid_name in line:
            print(line[:len(line)-1])
            count += 1

    if count == 0:
        print('contact not found')

    data.close()
    print()
    init_menu()

def find_contact_by_lastname_file(path):
    data = open(path, 'r', encoding='UTF-8')
    last_name = input('Enter last name ').capitalize()
    count = 0

    for line in data.readlines():
        if last_name in line:
            print(line[:len(line)-1])
            count += 1

    if count == 0:
        print('contact not found')

    data.close()
    print()
    init_menu()

def find_contact_by_number_file(path):
    data = open(path, 'r', encoding='UTF-8')
    phone = input('Enter phonenumber ')
    count = 0

    for line in data.readlines():
        if phone in line:
            print(line[:len(line)-1])
            count += 1

    if count == 0:
        print('contact not found')

    data.close()
    print()
    init_menu()

def change_contact_file(path):
    data = open(path, 'r+', encoding='UTF-8')
    old_data = data.read()

    print('Enter which contact you want to change')
    contact = input('Enter name ').capitalize()
    contact += ' ' + input('Enter middle name ').capitalize()
    contact += ' ' + input('Enter last name ').capitalize()
    contact += ' ' + input('Enter phone number ').capitalize()

    print('Enter new contact')
    changed_contact = input('Enter name ').capitalize()
    changed_contact += ' ' + input('Enter middle name ').capitalize()
    changed_contact += ' ' + input('Enter last name ').capitalize()
    changed_contact += ' ' + input('Enter phone number ').capitalize()

    data.seek(0)
    data.write(old_data.replace(contact, changed_contact))

    data.close()
    init_menu()

def delete_contact_file(path):
    data = open(path, 'r+', encoding='UTF-8')
    old_data = data.readlines()

    print('Enter which contact you want to delete')
    contact = input('Enter name ').capitalize()
    contact += ' ' + input('Enter middle name ').capitalize()
    contact += ' ' + input('Enter last name ').capitalize()
    contact += ' ' + input('Enter phone number ').capitalize() + '\n'

    for i in range(len(old_data)):
        if old_data[i] == contact:
            old_data.pop(i)
            print('Contact deleted!')

    open(path, 'w').close()
    data = open(path, 'r+', encoding='UTF-8')
    data.writelines(old_data)

    data.close()
    init_menu()


init_menu()
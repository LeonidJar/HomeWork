import view
import model
import text


def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_phonebook()
                view.print_message(text.load_successful)
            case 2:
                model.save_phonebook()
                view.print_message(text.save_successful)
            case 3:
                phone_book = model.get_phonebook()
                view.print_contacts(phone_book, text.load_error)
            case 4:
                contact = view.input_contact(text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_successful(name))
            case 5:
                pass
            case 6:
                pass
            case 7:
                phone_book = model.get_phonebook()
                index = view.input_index(text.index_del_contact, phone_book, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                break

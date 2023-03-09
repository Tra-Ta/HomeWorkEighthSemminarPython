from commands import read_file, read_file_to_list, ask_search, search_contact, find_contact, ask_user, add_contact, show, search_to_modify
from commands import change_contact, delete_contact, print_contacts


def main_menu(sprav):
    while True:
        user_choice = input(' \n'
                            '1 - Добавить контакт\n'
                            '2 - Найти контакт\n'
                            '3 - Изменить контакт\n'
                            '4 - Удалить контакт\n'
                            '5 - Показать весь справочник\n\n'
                            '0 - EXIT\n'
                            '\n')
        print()
        if user_choice == '1':
            add_contact(sprav)
        elif user_choice == '2':
            lst_contacts = read_file(file)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            change_contact(sprav)
        elif user_choice == '4':
            delete_contact(sprav)
        elif user_choice == '5':
            show(sprav)
        elif user_choice == '0':
            print('До свидания!')
            break


if __name__ == '__main__':
    file = 'phoneBook.txt'
    main_menu(file)
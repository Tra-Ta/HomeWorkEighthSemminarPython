from commands import main_menu, read_file, read_file_to_list, ask_search, search_contact, find_contact, ask_user, add_contact, show
from commands import search_to_modify, change_contact, delete_contact, print_contacts


if __name__ == '__main__':
    print(f'Добро пожаловать')
    file = 'phoneBook.txt'
    main_menu(file)
    
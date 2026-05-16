from contacts.utils import show_menu
from contacts.contact_manager import (
    add_contact,
    list_contacts,
    edit_contact,
    delete_contact,
    favorite_contact,
    list_favorite_contacts
)

while True:
    show_menu()

    option = input("Escolha uma opção: ")

    if option == "1":
        add_contact()

    elif option == "2":
        list_contacts()

    elif option == "3":
        edit_contact()

    elif option == "4":
        favorite_contact()

    elif option == "5":
        list_favorite_contacts()

    elif option == "6":
        delete_contact()

    elif option == "7":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")
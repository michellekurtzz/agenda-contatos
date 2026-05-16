from contacts.utils import show_menu
from contacts.contact_manager import (
    add_contact,
    list_contacts,
    edit_contact,
    delete_contact
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

    elif option == "6":
        delete_contact()

    elif option == "7":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")
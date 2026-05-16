from contacts.utils import show_menu
from contacts.contact_manager import add_contact, list_contacts

while True:
    show_menu()
    
    option = input("Escolha uma opção: ")

    if option == "1":
        add_contact()

    elif option == "2":
        list_contacts()

    elif option == "7":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")
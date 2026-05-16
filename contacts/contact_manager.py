from validations.validators import validate_contact_fields

contacts_list = []

def add_contact():
    name = input("Digite o nome: ")
    phone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    try:
        validate_contact_fields(name, phone, email)

    except Exception as error:
        print(error)
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "favorite": False
    }

    contacts_list.append(contact)
    print("Contato adicionado com sucesso")


def list_contacts():
    if not contacts_list:
        print("Nenhum contato cadastrado")
        return

    for contact in contacts_list:
        if contact["favorite"]:
            favorite_status = "Sim"
        else:
            favorite_status = "Não"

        print(
            f"Nome: {contact['name']} | "
            f"Telefone: {contact['phone']} | "
            f"Email: {contact['email']} | "
            f"Favorito: {favorite_status}"
        )


def edit_contact():
    name = input("Qual contato deseja editar? ")

    for contact in contacts_list:
        if contact["name"] == name:
            contact["name"] = input("Novo nome: ")
            contact["phone"] = input("Novo telefone: ")
            contact["email"] = input("Novo email: ")

            print("Contato editado com sucesso")
            return

    print("Contato não encontrado")


def delete_contact():
    name = input("Qual contato deseja deletar? ")

    for contact in contacts_list:
        if contact["name"] == name:
            contacts_list.remove(contact)
            print("Contato deletado com sucesso")
            return

    print("Contato não encontrado")


def favorite_contact():
    name = input("Qual contato deseja favoritar? ")

    for contact in contacts_list:
        if contact["name"] == name:

            if contact["favorite"]:
                print("Esse contato já está favoritado")
            else:
                contact["favorite"] = True
                print("Contato favoritado com sucesso")
            return

    print("Contato não encontrado")


def unfavorite_contact():
    name = input("Qual contato deseja remover dos favoritos? ")

    for contact in contacts_list:
        if contact["name"] == name:

            if not contact["favorite"]:
                print("Esse contato não está nos favoritos")
            else:
                contact["favorite"] = False
                print("Contato removido dos favoritos com sucesso")

            return

    print("Contato não encontrado")


def list_favorite_contacts():
    has_favorite = False

    for contact in contacts_list:
        if contact["favorite"]:
            print(contact["name"])
            has_favorite = True

    if not has_favorite:
        print("Nenhum contato favorito")
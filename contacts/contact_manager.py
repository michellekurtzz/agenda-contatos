contacts_list = []

def add_contact():
    name = input("Digite o nome: ")
    phone = input("Digite o telefone: ")
    email = input("Digite o email: ")

    if not name or not phone or not email:
        print("Todos os campos são obrigatórios")
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
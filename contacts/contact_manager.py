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
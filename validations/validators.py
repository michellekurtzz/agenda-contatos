from validations.exceptions import (
    InvalidEmailError,
    InvalidPhoneError,
    EmptyFieldError
)


def validate_contact_fields(name, phone, email):
    if not name or not phone or not email:
        raise EmptyFieldError(
            "Todos os campos são obrigatórios"
        )

    if not phone.isdigit():
        raise InvalidPhoneError(
            "Telefone deve conter apenas números"
        )

    if "@" not in email or "." not in email:
        raise InvalidEmailError(
            "Email inválido"
        )
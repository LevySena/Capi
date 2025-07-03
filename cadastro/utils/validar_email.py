from email_validator import validate_email, EmailNotValidError

def validar_email_com_biblioteca(email):
    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError as e:
        print(str(e))
        return False

##print(validar_email_com_biblioteca("exemplo@dominio.com"))
##print(validar_email_com_biblioteca("exemplo.invalido"))
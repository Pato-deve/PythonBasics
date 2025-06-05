def validar_num(password):
    return any(char.isnumeric() for char in password)

def validar_len(password):
    return len(password) >= 8

def validar_upper(password):
    return any(char.isupper() for char in password)

def validar_arroba(password):
    return any((char == "@") for char in password)

def validar_password(password):
    errores=[]
    if not validar_num(password):
        errores.append("Debe contener al menos 1 número.")
    if not validar_len(password):
        errores.append("Debe tener una longitud de al menos 8 caracteres.")
    if not validar_upper(password):
        errores.append("Debe tener al menos una mayuscula.")
    if not validar_arroba(password):
        errores.append("Debe tener un @")
    if not errores:
        return print("La contraseña es fuerte.")
    else:
        return print("Ingrese una nueva contraseña: ",errores)

def main():
    print("Una contraseña fuerte debe contener números, letras, mayusculas y contener al menos 8 caracteres.")
    password = input("Ingrese la contraseña: ")
    return validar_password(password)

if __name__ == "__main__":
    main()
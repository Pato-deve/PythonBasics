def validar_edad(edad):
    return edad >= 6 and edad <= 17

def main():
    try:
        edad = int(input("Ingrese la edad: "))
        if validar_edad(edad):
            return print("Edad escolar.")
        else:
            return print("Fuera de la edad escolar.")
    except ValueError:
        print("Se debe ingresar un número.")

if __name__ == "__main__":
    main()
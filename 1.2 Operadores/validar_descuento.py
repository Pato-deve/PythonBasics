def validar_compra(compra, premium):
    return compra >= 10000 and premium 

def main():
    canasta = float(input("Ingrese el valor de la compra: "))
    res = input("¿Tienen membresia? 0:No 1:Si ")
    cliente = res == "1"
    if validar_compra(canasta, cliente):
        return print("Aplica el descuento.")
    else:
        return print("No aplica el descuento.")

if __name__ == "__main__":
    main()
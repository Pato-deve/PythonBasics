def main():
    print("Es divisible cuando el cociente es un número entero.")
    try:
        dividendo = float(input("Ingrese el dividendo: "))
        divisor = float(input("Ingrese el divisor: "))
        
        if divisor == 0:
            return print("No se puede dividir entre 0.")
        
        cociente = dividendo / divisor
        print(f"El cociente de la division es: {cociente:.4f}")
        
        if (dividendo%divisor) == 0: 
            return print("Es divisible.")
        else:
            return print("No es divisible.")
    except ValueError:
        print("Entrada invalida. Se deben ingresar números.")

if __name__ == "__main__":
    main()
    

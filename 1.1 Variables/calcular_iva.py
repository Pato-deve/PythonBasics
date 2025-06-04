iva_porcentaje = 0.21

def impuesto_IVA(importe:float) -> float:
    # Calcula el IVA de un importe dado
    return importe * (1 + iva_porcentaje)

def main():
    try:
        precio_bruto= float(input('Importe a calcular: '))
        precio_final=impuesto_IVA(precio_bruto)
        print(f"El importe con un 21% incluido es: {precio_final:.2f}")
    except ValueError:
        print('El importe ingresado debe ser un número.')

if __name__ == "__main__":
    main()
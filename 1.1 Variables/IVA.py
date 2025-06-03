def impuesto_IVA(importe):
    # Calcula el IVA de un importe dado
    
    IVA = 0.21
    precio_final = importe+(importe * IVA)
    return precio_final

def main():
    try:
        precio_bruto= float(input('Importe a calcular: '))
        return print(impuesto_IVA(precio_bruto))
    except ValueError:
        print('El importe ingresado debe ser un número.')

main()
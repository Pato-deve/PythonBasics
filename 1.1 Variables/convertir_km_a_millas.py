def conversor_millas(km):
    # 1km = 0.621371
    mi = 0.621371
    millas = km * mi
    return millas

def main():
    try:
        kilometros= float(input('Ingrese los kilometros a convertir: '))
        return print(f"Los {kilometros} km equivalen a {conversor_millas(kilometros):.2f} millas.")
    except ValueError:
        print('El valor debe ser expresado en números.')
        
main()
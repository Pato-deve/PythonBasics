KM_A_MILLAS=0.621371

def conversor_millas(km:float)->float:
    return km * KM_A_MILLAS

def main():
    try:
        kilometros= float(input('Ingrese los kilometros a convertir: '))
        millas=conversor_millas(kilometros)
        print(f"{kilometros} kilometros equivalen a {millas:.2f} millas.")
    except ValueError:
        print('El valor debe ser expresado en números.')
        

if __name__ == "__main__":
    main()
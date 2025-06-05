def aritmetica(factor1, factor2):
    #Devolvemos los resultados de las opciones aritmeticas
    if factor2 == 0:
        raise ValueError("No se puede dividir entre 0.")
    
    resultados= {
        "multi":0,
        "division_float":0,
        "division_int":0,
        "suma":0,
        "resta":0,
        "modulo":0,
        "potencia":0,
    }
    resultados["multi"] = factor1 * factor2
    resultados["division_float"] = factor1 / factor2
    resultados["division_int"] = factor1 // factor2
    resultados["suma"] = factor1 + factor2
    resultados["resta"] = factor1 - factor2
    resultados["modulo"] = factor1 % factor2
    resultados["potencia"] = factor1 ** factor2
    return resultados


def main():
    factor_uno= int(input("Ingrese el primer factor: "))
    factor_dos= int(input("Ingrese el segundo factor: "))
    print(aritmetica(factor_uno, factor_dos))

if __name__ == "__main__":
    main()
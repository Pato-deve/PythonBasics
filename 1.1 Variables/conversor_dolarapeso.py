import requests
URL_API = 'https://dolarapi.com/v1/dolares/oficial'
PRECIO_FALLBACK=1200

def obtener_cotizacion():
    try:
        response = requests.get(URL_API, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data["venta"]
    except (requests.RequestException, KeyError):
        print("No se pudo obtener cotización oficial. Se brindara el precio actualizado hasta 3/6/2025")
        return PRECIO_FALLBACK

def main():
    try:
        venta= obtener_cotizacion()
        dolares = float(input("Ingrese la cantidad de dolares a convertir: "))
        pesos = dolares * venta
        print(f"{dolares}USD equivalen a {pesos:.2f} ARS")
    except ValueError:
        print("Debe ingresar valores numericos.")
        
    
if __name__ == "__main__":
    main()
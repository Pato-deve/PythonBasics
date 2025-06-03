import requests

def obtener_cotizacion():
    url = 'https://dolarapi.com/v1/dolares/oficial'
    response = requests.get(url, timeout=10)
    
    if response.status_code == 200:
        data = response.json()
        precio_venta = data["venta"]
        return precio_venta
    else:
        print("No se pudo obtener cotización oficial. Se brindara el precio actualizado hasta 3/6/2025")
        precio_venta=1160
        return precio_venta

def main():
    venta = obtener_cotizacion()
    dolares=float(input("¿Cuantos dolares quiere convertir? "))
    return print(f"Los dolares equivalen a: ${dolares*venta:.2f} pesos.")
    
main()
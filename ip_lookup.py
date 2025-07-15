import json
import requests

def solicitar_ips():
    archivo_json = "resultados_ips.json"
    resultados = []

    try:
        with open(archivo_json, "r") as f:
            resultados = json.load(f)
    except FileNotFoundError:
        pass

    while True:
        ip = input("Ingresa una IP pública (o escribe 'exit' para salir): ")
        if ip.lower() == "exit":
            break

        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data["status"] == "success":
                resultado = {
                    "query": data["query"],
                    "country": data["country"],
                    "regionName": data["regionName"],
                    "isp": data["isp"],
                    "lat": data["lat"],
                    "lon": data["lon"]
                }
                resultados.append(resultado)
                print(f"IP {ip} guardada.")
            else:
                print(f"Error: {data['message']}")
        else:
            print("No se pudo conectar con la API.")

    with open(archivo_json, "w") as f:
        json.dump(resultados, f, indent=4)

    print("Datos guardados en resultados_ips.json")

solicitar_ips()

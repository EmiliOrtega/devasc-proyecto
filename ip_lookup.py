import requests
import json

def obtener_info_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    respuesta = requests.get(url)
    return respuesta.json()

def main():
    resultados = []

    print("Consulta de IP pública (escribe 'exit' para salir)\n")

    while True:
        ip = input("Ingresa una IP pública: ").strip()
        if ip.lower() == "exit":
            break

        data = obtener_info_ip(ip)

        if data["status"] == "success":
            info = {
                "IP": ip,
                "País": data.get("country"),
                "Región": data.get("regionName"),
                "ISP": data.get("isp"),
                "Coordenadas": {
                    "Latitud": data.get("lat"),
                    "Longitud": data.get("lon")
                }
            }

            print(json.dumps(info, indent=4, ensure_ascii=False))
            resultados.append(info)
        else:
            print(f"Error: {data.get('message', 'No se pudo consultar la IP')}")
    
    with open("resultados_ips.json", "w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, indent=4, ensure_ascii=False)

    print("\nConsulta finalizada. Resultados guardados en 'resultados_ips.json'.")

if __name__ == "__main__":
    main()

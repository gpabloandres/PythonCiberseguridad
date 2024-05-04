import socket
import urllib.request

# Extraer el hostname de mi equipo

hostname = socket.gethostname()

print(f"Mi hostname es: {hostname}")

# Extraer la dirección IP privada de mi equipo

internal_ip_adress = socket.gethostbyname(hostname)

print(f"Mi dirección IP privada es: {internal_ip_adress}")

# Extraer la dirección IP pública de mi equipo

# external_ip_adress = urllib.request.urlopen('').read().decode('utf8')

# print(f"Mi dirección IP privada es: {external_ip_adress}")

# Extraer la dirección pública de un servidor externo

ip_adress_google = socket.getaddrinfo('google.com', 80)

print(f"La dirección IP pública del servidor de Google es: {ip_adress_google}")
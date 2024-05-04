import nmap

scanner = nmap.PortScanner()

ip = input("Introduzca una dirección IP: ")

print(f"Ingresaste esta dirección IP: {ip}")

scanner.scan(ip)

print(scanner.all_hosts())
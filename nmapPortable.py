#Script con el que podemos escanear los puertos abiertos de un hosts. En la MITRE ATT&CK se recoge como la tecnica T1046
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Introducimnos la ip a la que quermemos escanear
objetivo = input("Introduzca ip objetivo: ")


target_ip = socket.gethostbyname(objetivo)

#En esta funcion es en la que nos conectamos mediante los sockets y comprobamos que el puertos esta abierto en caso de que este nos lo muestra
def portScan(port):
	try:
	    s.connect((target_ip, port))
	    return True
	except:
	    return False

for port in range(65535):
	if portScan(port):
	    print(f'Puerto {port} esta abierto')

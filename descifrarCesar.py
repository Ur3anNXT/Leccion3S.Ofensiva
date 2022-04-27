#Con este script podemos descrifar el mensaje generado con cifrado Cesar ojo! Tenemos que saber que desplazamiento tiene sino estamos rip
#Introducimos el mensaje cifrado. En la MITRE ATT&CK se recoge como fuerza bruta (T1110)
texto = input("Introduzca el mensaje cifrado: ")

#Definimos el diccionario con el que haremos la fuerza bruta
caracts = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910"

#Comenzamos con el descrifrado donde lo que vayamos traduciendo lo introducimos en la variable traducido
for key in range (len(caracts)):
	traducido = ""
	
	#Ahora lo que haremos sera comporbar si el caracter actual se encuentra en el diccionario, esto lo haremos con el metodo .find() representado por elemIndex
	for elem in texto:
		if elem in caracts:
			elemIndex = caracts.find(elem)
			tradIndex = elemIndex - key
			
			if tradIndex < 0:
				tradIndex = tradIndex + len(caracts)
			
			traducido = traducido + caracts[tradIndex]
		else:
			traducido = traducido + elem
		
		print("key #%s: %s" % (key, traducido))


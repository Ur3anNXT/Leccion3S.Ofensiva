#Con este script podemos cifrar en Cesar cualquier mensaje

#Introduzimos el mensaje que queremos cifrar
texto = input("Introduzca mensaje a cifrar: ")

#Definimos las letras y numeros para la fuerza bruta
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910"

#Introducimos el valor de desplazamiento
desplazamiento = int(input("Introduzca valor de desplazamiento: "))
cifrado=""

#Iniciamos el metodo de crifrado usando la variable cifrado para ir introduciendo las letras y crear el mensaje
for c in texto:
	if c in abc:
		cifrado += abc [(abc.index(c)+desplazamiento) % (len(abc))]
	else:
		cifrado += c

#Imprimimos el texto cifrado
print("Mensaje cifrado: ", cifrado)

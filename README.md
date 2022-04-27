
# Leccion 3 Seguridad Ofensiva MITRE ATT&CK

En este caso encontramos diferentes scripts realizados para la lección 3 de Seguridad Ofensiva donde se aplican técnicas recogidas en la MITRE ATT&amp;CK


## Command and Scripting interpreter (T1059)

Esta técnica nos habla sobre cómo se puede abusar de intérpretes de scripts para ejecutar comandos, script o archivos binarios. Dichas interfaces usan enjuagues qué brindan formas de interactuar con los sistemas y son una característica común en muchas de las plataformas, dichos lenguajes por ejemplo pueden ser, python, bash, perl, php, etc. 

En mi caso en el script qué se adjunta llamado imNotAReverseShell.sh encontramos la linea de comandos qué se tendra qué ejecutar en la victima mientras se está en escucha por el puerto indicado para poder conseguir una reverse Shell. Cabe indicar qué en el script se tendría qué indicar la ip de nuestro equipo y el puerto por el qué queremos recibir la reverse shell.

## Deployment

Lo primero que tendremos que hacer es cambiar los parametros necesarios en el script 
para poder mandarnos la reverse shell a nosotros. Dichos parametros seran la ip y el puerto
donde tendremos que poner los correspondientes a nuestra maquina.

```bash
  chmod +x imNotAReverseShell.sh
```
A continuación lo que haremos sera ponernos a la escucha por el puerto que pusimos en el script.

```bash
  nc -lvpn 3000
```
Con esto ya simplemente tendremos que esperar a que la victima ejecute el script o en caso 
de poder hacerlo nosotros ya sea mediante LFI o en algun entorno de pruebas para que tuvieramos
nuestra reverse shell.


## Network Service Discovery (T1046)

Nos encontramos frente a una serie de técnicas con la qué podemos intentar obtener una lista de servicios que se ejecutan en hosts remotos y dispositivos de infraestructura de red local, incluidos aquellos que pueden ser vulnerables a la explotación remota de software. Los métodos comunes para adquirir esta información incluyen escaneos de puertos o vulnerabilidades se pueden hacer con scripts creados por ejemplo con el caso de Chimera qué creo un script en Python con el comando get -b -e -p con el qué se podía escanear la red, luego lo introdujeron en un ejecutable de Windows con el qué escaneaban rangos de ip por HTTP. 

En nuestro caso crearemos un script en Python con el qué podremos escanear los puertos qué estén abiertos de un host qué elijamos (Hay dos maneras una con el módulo de Nmap con el qué tendremos más opciones y otro más básica jugando con Sockets). El script se llamará Word.exe y lo haremos mediante el uso de Sockets en Python.

## Deployment

Lo primero que tendremos que hacer es cambiar los parametros necesarios en el script 
para poder mandarnos la reverse shell a nosotros. Dichos parametros seran la ip y el puerto
donde tendremos que poner los correspondientes a nuestra maquina.

```bash
  chmod +x nmapPortable.py
```
Luego simplemente lo ejecutamos, ponemos la ip de la victima y se escanearan los puertos
en busca de los que esten abiertos.

```bash
  chmod +x nmapPortable.py
```

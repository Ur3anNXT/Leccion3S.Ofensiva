# Leccion3S.Ofensiva
En este caso encontramos diferentes scripts realizados para la lección 3 de Seguridad Ofensiva donde se aplican técnicas recogidas en la MITRE ATT&amp;CK

Command and Scripting interpreter 

Esta técnica nos habla sobre cómo se puede abusar de intérpretes de scripts para ejecutar comandos, script o archivos binarios. Dichas interfaces usan enjuagues qué brindan formas de interactuar con los sistemas y son una característica común en muchas de las plataformas, dichos lenguajes por ejemplo pueden ser, python, bash, perl, php, etc. 

En mi caso en el script qué se adjunta llamado imNotAReverseShell.sh encontramos la linea de comandos qué se tendra qué ejecutar en la victima mientras se está en escucha por el puerto indicado para poder conseguir una reverse Shell. Cabe indicar qué en el script se tendría qué indicar la ip de nuestro equipo y el puerto por el qué queremos recibir la reverse shell.

Network Service Discovery

Nos encontramos frente a una serie de técnicas con la qué podemos intentar obtener una lista de servicios que se ejecutan en hosts remotos y dispositivos de infraestructura de red local, incluidos aquellos que pueden ser vulnerables a la explotación remota de software. Los métodos comunes para adquirir esta información incluyen escaneos de puertos o vulnerabilidades se pueden hacer con scripts creados por ejemplo con el caso de Chimera qué creo un script en Python con el comando get -b -e -p con el qué se podía escanear la red, luego lo introdujeron en un ejecutable de Windows con el qué escaneaban rangos de ip por HTTP. 

En nuestro caso crearemos un script en Python con el qué podremos escanear los puertos qué estén abiertos de un host qué elijamos (Hay dos maneras una con el módulo de Nmap con el qué tendremos más opciones y otro más básica jugando con Sockets). El script se llamará Word.exe y lo haremos mediante el uso de Sockets en Python.

Brute force

En este caso nos encontramos frente a una técnica usada para obtener acceso a las cuentas cuando se desconocen las contraseñas o cuando se obtienen hash de contraseñas. Sin el conocimiento de la contraseña de una cuenta o conjunto de cuentas, un adversario puede adivinar sistemáticamente la contraseña utilizando un mecanismo repetitivo o iterativo. Las contraseñas de fuerza bruta pueden tener lugar a través de la interacción con un servicio que verificará la validez de esas credenciales o fuera de línea con los datos de credenciales adquiridos previamente, como hash de contraseñas. 

En nuestro caso usare un script creado durante mi formación en ASIR qué consta de un descifrado Cesar mediante fuerza bruta, pero en nuestro caso primeramente le pasaremos un script con el qué ciframos en Cesar para previamente tenemos es hash en César pasar por el Descifrado donde usaremos la fuerza bruta para sacar el mensaje descifrado (para ello usaremos la misma cadena de caracteres qué cuando la ciframos).

Para más  informacion: https://drive.google.com/file/d/1pEl8tzXL25FxgFIngT9GpTsUN2mqKpyr/view?usp=sharing

# ROS_Project_Publishers-Suscribers

_Toda la documentación en la que se basa este proyecto se encuentra en la página web de ROS. En este proyecto se realiza la conexion de 8 nodos en los cuales se envian diferentes tipos de datos entre ellos y posteriormente se genere envio y recepcion de datos desde un Arduino Uno (9 nodos en total incluyendo el de arduino). Recomiendo instalar previamente Arduino y el nodo serial arduino ros para poder trabajar adecuadamente_

## Estructura - Nodos en Linux

Los 9 nodos de este proyecto envian, reciben y procesan información, cada script de los nodos cuenta con sus comentarios donde se explica el funcionamiento de cada uno. De esta manera solo presentare aquí una breve descripción de cada nodo y la ejecución de los nodos mediante terminal.

El paquete contiene nodos ROS de la A a la H que publican y suscriben diferentes tipos de variables, incluidas Bool, Int16, FLoat32, Char y String. Finalmente, hay un Nodo con comunicación serial entre ROS y Ardunio para implementación en el mundo real.

(H -> ARDUINO, ARDUINO -> A), estos nodos ROS están destinados a utilizar un controlador de lógica difusa para considerar 3 señales y tomar una decisión para un actuador final.

* Nodo A: Este nodo se suscribe a un topic string del nodo de Arduino y divide la cadena recibida según el sensor. Publica cada valor en un topic diferente: Bool, Int16 y Float32.

* Nodo B: Este nodo se suscribe a un topic Bool del Nodo A, calcula el nivel bajo/medio/alto mediante una logica semidifusa. Publica un String que contiene cada uno de los valores calculados.

* Nodo C: Este nodo se suscribe a un topic Int del Nodo A, calcula el nivel bajo/medio/alto mediante una logica semidifusa. Publica un String que contiene cada uno de los valores calculados.

* Nodo D: Este nodo se suscribe a un topic Float del Nodo A, calcula el nivel bajo/medio/alto mediante una logica semidifusa. Publica un String que contiene cada uno de los valores calculados.

* Nodo E: Este nodo se suscribe a un topic String del Nodo B, extrae el nivel bajo/medio/alto y compara sus valores mediante una logica semidifusa. Finalmente, publica un carácter mediante string con la letra de mayor valor.

* Nodo F: Este nodo se suscribe a un topic String del Nodo C, extrae el nivel bajo/medio/alto y compara sus valores mediante una logica semidifusa. Finalmente, publica un carácter mediante string con la letra de mayor valor.

* Nodo G: Este nodo se suscribe a un topic String del Nodo D, extrae el nivel bajo/medio/alto y compara sus valores mediante una logica semidifusa. Finalmente, publica un carácter mediante string con la letra de mayor valor.

* Nodo H: Este nodo se suscribe a un topic String de los Nodos E, F y G, recibe las letras según cada nodo y realiza una logica semidifusa tomando una decisión según corresponda para el actuador final. Finalmente, publica un string de un solo caracter que contiene la desición.

* Nodo Arduino: Este nodo se suscribe a un topic String del Nodo H, usa el valor para configurar una posición del servomotor, también toma el valor de 3 sensores y publica un String con el valor de los sensores.


### Ejecucion

_1)Para ejecutar el codigo se debe en el terminal ejecutar de la siguiente manera_

* En el primer terminal se ejecuta roscore
```
roscore
```

* En un terminal diferente para cada script se ejecuta la siguiente sentencia
```
rosrun Carpeta_nodo Nombre_script.py
```

* En un terminal diferente para visulaizar todos los nodos y que efectivamente esten conectados se ejecuta la siguiente sentencia
```
rqt_graph
```


### Ejecución Nodo Arduino

Para ejecutar el nodo de Arduino, es necesario dar permisos al puerto de entrada de la tarjeta, para ello se hace lo siguiente:

_1) Una vez esta el codigo listo se debe ejecutar las siguientes sentencias en el terminal_
```
sudo chmod 777 /dev/ttyACM0 # se le dan los permisos al puerto (El cero puede cambiar esta informacion la entrega la sentencia anterior)
```

_2) Se carga el codigo en el arduino y posteriormente se ejecuta las siguientes sentencias de ROS_
```
roscore #nucleo de ROS se debe correr en un terminal

rosrun rosserial_python serial_node.py /dev/ttyACM0 # En un segundo terminal se corre esta sentencia (Nota: Para que esto sirva se debe instalar la libreria rosserial)
```

## Autor

* Eymer S. Tapias

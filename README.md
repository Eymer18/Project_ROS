# Project_ROS

_Toda la documentación en la que se basa este proyecto se encuentra en la página web de ROS. En este proyecto se realiza la conexion de 8 nodos en los cuales se envian diferentes tipos de datos entre ellos y posteriormente se genere envio y recepcion de datos desde un Arduino Uno. Recomiendo instalar previamente Arduino y el nodo serial arduino ros para poder trabajar adecuadamente_

## Estructura - Nodos en Linux

Los 9 nodos de este proyecto envian, reciben y procesan información, cada script de los nodos cuenta con sus comentarios donde se explica el funcionamiento de cada uno. De esta manera solo presentare aquí la ejecución de los nodos mediante terminal.  

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


## Ejecución Nodo Arduino

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

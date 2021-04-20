#!/usr/bin/env python
					#Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy				#Importar libreria de ros
from std_msgs.msg import String		#libreria std_msgs para poder usar cadenas string

e = None				#Declaracion de variable
char_c = ""				#Declaracion de cadena vacia

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
    global e				# Se declara que la variable es global 
    e = data.data			# Se guarda el valor que recibe en la  variable


def Nodo_E():
    global e
    global char_c
    rospy.init_node('Nodo_E', anonymous=False)			#Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('String_E', String, callback)		#El Nodo_E se suscribe al topic String_E, de tipo String y llama a callback.
    
    pub7 = rospy.Publisher('Char_H1', String, queue_size=10)	#El Nodo_F publica el topic Char_H2, de tipo String.
    rate = rospy.Rate(0.5) # 0.5hz				#Se establece un bucle de velocidad deseada 
    while not rospy.is_shutdown():
     
						#pregunta si es diferente de tipo None 
	if e!=None:
		e1=e.split('/') 		#Split() sirve para dividir una cadena segun el separador que se indique 
        
		if e1[0] == "Alto=100%":
			char_c = "A"        
		elif e1[1] == "Bajo=100%":
			char_c = "B"

        
        rospy.loginfo(rospy.get_caller_id()+" "+char_c)		#imprime mensaje en terminal de la cadena especificada
        pub7.publish(char_c)
        rate.sleep()						#Mantiene el bucle en la velocidad deseada


if __name__ == '__main__':
    try:
        Nodo_E()
    except rospy.ROSInterruptException:
        pass

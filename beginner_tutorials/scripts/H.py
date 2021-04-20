#!/usr/bin/env python
                                          #Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy                              #Importar libreria de ros
from std_msgs.msg import String           #libreria std_msgs para poder usar cadenas string

h1 = None
h2 = None
h3 = None
string_str=""

def callback1(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)  #imprime mensaje en terminal de lo que recibe, con el nombre del nodo
    global h1
    h1 = data.data

def callback2(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)  #imprime mensaje en terminal de lo que recibe, con el nombre del nodo
    global h2
    h2 = data.data

def callback3(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)  #imprime mensaje en terminal de lo que recibe, con el nombre del nodo
    global h3
    h3 = data.data

def Nodo_H():

    global string_str
    
    rospy.init_node('Nodo_H', anonymous=False)                      #Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('Char_H1', String, callback1)                   #El Nodo_H se suscribe topic Char_H1, de tipo String, callback1.
    rospy.Subscriber('Char_H2', String, callback2)                   #El Nodo_H se suscribe topic Char_H2, de tipo String, callback2.
    rospy.Subscriber('Char_H3', String, callback3)                   #El Nodo_H se suscribe topic Char_H3, de tipo String, callback3.
    
    pub10 = rospy.Publisher('String_Arduino', String, queue_size=10) #El nodo publica el tema String_Arduino utilizando mensajes tipo String
    rate = rospy.Rate(0.2) # 0.2hz                                    #Se establece un bucle de velocidad deseada
    while not rospy.is_shutdown():
								#Pregunta si es diferente de tipo None
	if h1!=None and h2!=None and h3!=None: 
								#Arbol de decisiones
		if h1=="B" and h2=="B" and h3=="B":
			string_str="0"

		elif h1=="A" and h2=="A" and h3=="A":
			string_str="180"

		elif h1=="B" and h2=="M" and h3=="M":
			string_str="60"

		elif h1=="B" and h2=="A" and h3=="A":
			string_str="120"

		elif h1=="B" and h2=="M" and h3=="A":
			string_str="90"

		elif h1=="B" and h2=="A" and h3=="M":
			string_str="90"

		elif h1=="A" and h2=="M" and h3=="M":
			string_str="120"

		elif h1=="A" and h2=="B" and h3=="B":
			string_str="30"

		elif h1=="A" and h2=="M" and h3=="A":
			string_str="150"

		elif h1=="A" and h2=="A" and h3=="M":
			string_str="150"

		elif h1=="B" and h2=="B" and h3=="M":
			string_str="30"

		elif h1=="B" and h2=="B" and h3=="A":
			string_str="60"

		elif h1=="B" and h2=="M" and h3=="B":
			string_str="30"

		elif h1=="B" and h2=="A" and h3=="B":
			string_str="60"

		elif h1=="A" and h2=="B" and h3=="M":
			string_str="90"

		elif h1=="A" and h2=="B" and h3=="A":
			string_str="120"

		elif h1=="A" and h2=="M" and h3=="B":
			string_str="90"

		elif h1=="A" and h2=="A" and h3=="B":
			string_str="120"

        rospy.loginfo(rospy.get_caller_id()+" El angulo del servo es "+string_str) #imprime mensaje en terminal de la cadena especificada
        pub10.publish(string_str)                                 		    #publica una cadena para el topic String_Arduino
        rate.sleep()                                               		   #Mantiene el bucle en la velocidad deseada
    

if __name__ == '__main__':
    try:
        Nodo_H()                                                    #El try cath se usa para que no continue ejecutando
                                                                    #codigo accidentalmente si el nodo se suspende
    except rospy.ROSInterruptException:
        pass

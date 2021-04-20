#!/usr/bin/env python
                                          #Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy                              #Importar libreria de ros
from std_msgs.msg import Bool             #libreria std_msgs para poder usar variables booleanas
from std_msgs.msg import String           #libreria std_msgs para poder usar cadenas string

b = None

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)  #imprime mensaje en terminal de lo que recibe, con el nombre del nodo 
    global b
    b = data.data

def Nodo_B():

    rospy.init_node('Nodo_B', anonymous=False)                      #Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('Bool_B', Bool, callback)                      #El Nodo_B se suscribe al tema Bool_B, de tipo bool y llama a otra fun.

    pub4 = rospy.Publisher('String_E', String, queue_size=10)       #El nodo publica el tema String_E utilizando mensajes tipo String
    rate = rospy.Rate(1) # 1hz                                      #Se establece un bucle de velocidad deseada (1 vez por segundo)
    while not rospy.is_shutdown():
        
        if b == True:
            string_str = "Alto=100%/Bajo=0%"

        elif b == False:
            string_str = "Alto=0%/Bajo=100%"
        
        else:
            string_str = "" 

        rospy.loginfo(rospy.get_caller_id()+" "+string_str)         #imprime mensaje en terminal de la cadena especificada 
        pub4.publish(string_str)                                    #publica una cadena para el tema String_E
        rate.sleep()                                                #Mantiene el bucle en la velocidad deseada 

if __name__ == '__main__':
    try:
        Nodo_B()                                                    #El try cath se usa para que no continue ejecutando
                                                                    #codigo accidentalmente si el nodo se suspende
    except rospy.ROSInterruptException:
        pass

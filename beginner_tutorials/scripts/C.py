#!/usr/bin/env python
					#Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy				#Importar libreria de ros
from std_msgs.msg import Int16		#libreria std_msgs para poder usar enteros de 16 bits
from std_msgs.msg import String		#libreria std_msgs para poder usar cadenas string

c = None

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data)
    global c						# Se declara que la variable es global 
    c = data.data					# Se guarda el valor que recibe en la  variable

def Nodo_C():

    rospy.init_node('Nodo_C', anonymous=False)			#Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('Int_C', Int16, callback)			#El Nodo_C se suscribe al topic Int_C, de tipo Int16 y llama a callback.

    pub5 = rospy.Publisher('String_F', String, queue_size=10)	#El Nodo_C publica el topic String_F, de tipo String.
    rate = rospy.Rate(1) # 1hz					#Se establece un bucle de velocidad deseada 
    while not rospy.is_shutdown():     
   								#logica fuzzy
        if c<=50:
            string_str = "Alto=0%/Medio=0%/Bajo=100%"
        
        if c>50 and c<=70:
               c1 = -5*c+350					#ecuaciones de la linea recta
               c2 = 5*c-250
               if c1>c2: 
                      string_str = "Alto=0%/Medio="+str(c2)+"%/Bajo="+str(c1)+"%"  
               elif c1<c2: 
                      string_str = "Alto=0%/Medio="+str(c2)+"%/Bajo="+str(c1)+"%"

        if c>70 and c<=110:
               string_str = "Alto=0%/Medio=100%/Bajo=0%"	#Cadena a enviar
        
        if c>110 and c<=130:
               c1 = -5*c+650
               c2 = 5*c-550
               if c1>c2: 
                      string_str = "Alto="+str(c2)+"%/Medio="+str(c1)+"%/Bajo=0%"  
               elif c1<c2:
                      string_str = "Alto="+str(c2)+"%/Medio="+str(c1)+"%/Bajo=0%"
        
        if c>130 and c<=180:
                 string_str = "Alto=100%/Medio=0%/Bajo=0%" 

       
        rospy.loginfo(rospy.get_caller_id()+" "+string_str)	#imprime mensaje en terminal de la cadena especificada
        pub5.publish(string_str)				#publica una cadena para el tema String_Arduino
        rate.sleep()						#Mantiene el bucle en la velocidad deseada


if __name__ == '__main__':
    try:
        Nodo_C()
    except rospy.ROSInterruptException:
        pass

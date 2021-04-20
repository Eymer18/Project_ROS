#!/usr/bin/env python
					#Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy				#Importar libreria de ros
from std_msgs.msg import Float32	#libreria std_msgs para poder usar flotantes de 32 bits
from std_msgs.msg import String		#libreria std_msgs para poder usar cadenas string

d = None

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', round(data.data,2))
    global d					# Se declara que la variable es global
    d = round(data.data,2)			# Se guarda el valor que recibe en la  variable y se redondea a 2 decimales 

def Nodo_D():

    rospy.init_node('Nodo_D', anonymous=False)			#Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('Float_D', Float32, callback)		#El Nodo_D se suscribe al topic Float_D, de tipo Float32 y llama a callback.

    pub6 = rospy.Publisher('String_G', String, queue_size=10)	#El Nodo_C publica el topic String_F, de tipo String.
    rate = rospy.Rate(1) # 1hz					#Se establece un bucle de velocidad deseada 
    while not rospy.is_shutdown():
           							#logica fuzzy
        if d<=1.25:
            string_str = "Alto=0%/Medio=0%/Bajo=100%"
        
        if d>1.25 and d<=2.1:
               d1 = round(-117.65*d+247.065,0)			#ecuaciones de la linea recta
               d2 = round(117.65*d-147.0625,0)
               if d1>d2: 
                      string_str = "Alto=0%/Medio="+str(d2)+"%/Bajo="+str(d1)+"%"  
               elif d1<d2: 
                      string_str = "Alto=0%/Medio="+str(d2)+"%/Bajo="+str(d1)+"%"

        if d>2.1 and d<=2.9:
               string_str = "Alto=0%/Medio=100%/Bajo=0%"	#Cadena a enviar
        
        if d>2.9 and d<=3.75:
               d1 = round(-117.65*d+441.1875,0)
               d2 = round(117.65*d-341.185,0)
               if d1>d2: 
                      string_str = "Alto="+str(d2)+"%/Medio="+str(d1)+"%/Bajo=0%"  
               elif d1<d2:
                      string_str = "Alto="+str(d2)+"%/Medio="+str(d1)+"%/Bajo=0%"
        
        if d>3.75 and d<=5:
                 string_str = "Alto=100%/Medio=0%/Bajo=0%" 


        rospy.loginfo(rospy.get_caller_id()+" "+string_str)	#imprime mensaje en terminal de la cadena especificada
        pub6.publish(string_str)				#publica una cadena para el topic especficado
        rate.sleep()						#Mantiene el bucle en la velocidad deseada


if __name__ == '__main__':
    try:
        Nodo_D()
    except rospy.ROSInterruptException:
        pass

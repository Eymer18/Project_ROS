#!/usr/bin/env python
                                          #Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy                              #Importar libreria de ros
import random                             #Importar libreria para usar randomicos
from std_msgs.msg import Bool             #libreria std_msgs para poder usar variables booleanas  
from std_msgs.msg import Int16            #libreria std_msgs para poder usar valores enteros de 8 bits  
from std_msgs.msg import Float32          #libreria std_msgs para poder usar valores flotantes de 32 bits
from std_msgs.msg import String

a = None				  #Declaracion de variable
bool_b=""				  #Declaracion de cadena vacia 
int_i=""
float_f=""


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + ' %s', data.data) 
    global a					# Se declara que la variable es global
    a = data.data				# Se guarda el valor que recibe en la  variable

def Nodo_A():                                                        
    
    global bool_b				# Se declara que la cadena es global
    global int_i
    global float_f

    rospy.init_node('Nodo_A', anonymous=False)                      #Inicia e indica a rospy el nombre del nodo, IMPORTANTE!

    rospy.Subscriber('N_Ardu', String, callback)

    pub1 = rospy.Publisher('Bool_B', Bool, queue_size=1)            #El nodo publica el tema Bool_B utilizando mensajes tipo Bool 
    pub2 = rospy.Publisher('Int_C', Int16, queue_size=10)           #El nodo publica el tema Int_C utilizando mensajes tipo Int8
    pub3 = rospy.Publisher('Float_D', Float32, queue_size=10)       #El nodo publica el tema Float_D utilizando mensajes tipo Float32
    
    rate = rospy.Rate(1) # 10hz                                     #Se establece un bucle de velocidad deseada (10 veces por segundo)
    while not rospy.is_shutdown():                                  #Bucle que verifica si el programa debe salir (ejemplo si hay Ctrl+C)

	if a!=None:

		a1=a.split('/')					#Split() sirve para dividir una cadena segun el separador que se indique

		ab=a1[0].split('=')
		ai=a1[1].split('=')
		af=a1[2].split('=')	
		
		bool_b=int(ab[1])				#convierte el valor a entero
								#Desicion dependiendo del valor
		if bool_b==0:
			bool_b=False
		elif bool_b==1:
			bool_b=True

		int_i=int(ai[1])				#convierte el valor a entero
		float_f=float(af[1])				#convierte el valor a flotante

                      
        rospy.loginfo(rospy.get_caller_id()+" "+str(bool_b))
        rospy.loginfo(rospy.get_caller_id()+" "+str(int_i))
        rospy.loginfo(rospy.get_caller_id()+" "+str(float_f))            #imprime mensaje en terminal de la variable especificada 
        pub1.publish(bool_b)                                        #publica un booleano para el tema Bool_B  
        pub2.publish(int_i)                                       
        pub3.publish(float_f)                                       #publica un flotante para el tema Float_D
        rate.sleep()                                                #Mantiene el bucle en la velocidad deseada 

if __name__ == '__main__':
    try:
        Nodo_A()                                                    #El try cath se usa para que no continue ejecutando
                                                                    #codigo accidentalmente si el nodo se suspende
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python
					#Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy				#Importar libreria de ros
from std_msgs.msg import String		#libreria std_msgs para poder usar cadenas string
from std_msgs.msg import Char

g = None				#Declaracion de variable
char_c = ""				#Declaracion de cadena vacia

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    global g						# Se declara que la variable es global 
    g = data.data					# Se guarda el valor que recibe en la  variable

def Nodo_G():

    global char_c

    rospy.init_node('Nodo_G', anonymous=False)			#Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('String_G', String, callback)		#El Nodo_G se suscribe al topic String_G, de tipo String y llama a callback.
    
    pub9 = rospy.Publisher('Char_H3', String, queue_size=10)	#El Nodo_F publica el topic Char_H2, de tipo String.
    rate = rospy.Rate(0.5) # 0.5hz				#Se establece un bucle de velocidad deseada 
    while not rospy.is_shutdown():
							
	if g!=None:

	        g1=g.split('/')				#Split() sirve para dividir una cadena segun el separador que se indique 
	
		ga=g1[0].split('=')
		gm=g1[1].split('=')
		gb=g1[2].split('=')	

		A=ga[1].split('%')
		M=gm[1].split('%')
	        B=gb[1].split('%')

		a=float(A[0])				#convierte a flotante el valor guradado en dicha posicion del vecto
		m=float(M[0])
		b=float(B[0])
							#arbol de decision 
		if a==0.0 and m==0.0 and b==100.0:
	            char_c = "B"
	        
	        if a<=50.0 and m<=50.0 and b>=50.0:
	            char_c = "B"

	        if a==0.0 and m==100.0 and b==0.0:
	            char_c = "M"			#Caracter a enviar
	        
	        if a<=50.0 and m>=50.0 and b<=50.0:
	            char_c = "M"
        
	        if a==100.0 and m==100.0 and b==0.0:
	            char_c = "A" 	

		if a>=50.0 and m<=50.0 and b<=50.0:
	            char_c = "A"		

        
        rospy.loginfo(rospy.get_caller_id()+" "+char_c)		#imprime mensaje en terminal de la cadena especificada
        pub9.publish(char_c)
        rate.sleep()						#Mantiene el bucle en la velocidad deseada


if __name__ == '__main__':
    try:
        Nodo_G()
    except rospy.ROSInterruptException:
        pass

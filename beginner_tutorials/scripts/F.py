#!/usr/bin/env python
					#Primera linea se asegura de ejecutar la secuencia de comandos como comandos de python
import rospy				#Importar libreria de ros
from std_msgs.msg import String		#libreria std_msgs para poder usar cadenas string
from std_msgs.msg import Char

f = None				#Declaracion de variable
char_c = ""

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    global f							# Se declara que la variable es global 
    f = data.data						# Se guarda el valor que recibe en la  variable

def Nodo_F():	

    global char_c    

    rospy.init_node('Nodo_F', anonymous=False)			#Inicia e indica a rospy el nombre del nodo

    rospy.Subscriber('String_F', String, callback)		 #El Nodo_F se suscribe al topic String_F, de tipo String y llama a callback.
    
    pub8 = rospy.Publisher('Char_H2', String, queue_size=10)	#El Nodo_F publica el topic Char_H2, de tipo String.
    rate = rospy.Rate(0.5) # 0.5hz				#Se establece un bucle de velocidad deseada 
    while not rospy.is_shutdown():

	if f!=None:

	        f1=f.split('/')                  #Split() sirve para dividir una cadena segun el separador que se indique 
	
		fa=f1[0].split('=')
		fm=f1[1].split('=')
		fb=f1[2].split('=')	

		A=fa[1].split('%')
		M=fm[1].split('%')
	        B=fb[1].split('%')

		a=int(A[0])			#convierte a entero el valor guradado en dicha posicion del vector
		m=int(M[0])
		b=int(B[0])
						#Decisiones dependiendo del valor que llego
		if a==0 and m==0 and b==100:
	            char_c = "B"
	        
	        if a<=50 and m<=50 and b>=50:
	            char_c = "B"

	        if a==0 and m==100 and b==0:
	            char_c = "M"
	        
	        if a<=50 and m>=50 and b<=50:
	            char_c = "M"		#Caracter a enviar
        
	        if a==100 and m==100 and b==0:
	            char_c = "A" 	

		if a>=50 and m<=50 and b<=50:
	            char_c = "A"


        rospy.loginfo(rospy.get_caller_id()+" "+char_c)		#imprime mensaje en terminal de la cadena especificada
        pub8.publish(char_c)
        rate.sleep()						#Mantiene el bucle en la velocidad deseada


if __name__ == '__main__':
    try:
        Nodo_F()
    except rospy.ROSInterruptException:
        pass

//rosrun rosserial_python serial_node.py /dev/ttyACM0
//sudo chmod a+rw /dev/ttyACM0    or    sudo chmod 777 /dev/ttyACM0 

#include <Servo.h>             //libreria Servomotor
#include <ros.h>               //libreria ros
#include <std_msgs/String.h>   //libreria mensajes tipo string

//--------Decl. Variables-----//
bool val_bool=false;
int val_int=0;
float val_float=0.0;
String valor="";
String Send_data="";
char msg[30];

Servo Servomotor;

ros::NodeHandle NodoArduino;   //Declaración del nodo
std_msgs::String str_msg;      //Decla. variable de tipo string

ros::Publisher N_Ardu("N_Ardu", &str_msg); //Publicador declaración

void R_msg(const std_msgs::String& data)
 {
   valor=data.data;                     //guarda lo que recibio en un string
   Servomotor.write(valor.toInt());     //Envia al servo el valor en formato entero
 }

ros::Subscriber<std_msgs::String> sub("String_Arduino", R_msg);  //Suscriptor declaración

void setup() 
{
  pinMode(A0, INPUT);  //Pot1-Int
  pinMode(A1, INPUT);  //Pot2-Float
  pinMode(A2, INPUT);   //Botón-Bool
  
  Servomotor.attach(9); //Pin del servomotor
  
  NodoArduino.initNode();         //Inicializar nodo en la tarjeta 
  NodoArduino.advertise(N_Ardu);  //Indica el topic
  NodoArduino.subscribe(sub);     //Se suscribe al topic antes especificado
}

void loop() 
{
    // reading values to send ROS
  val_bool = digitalRead(A2);                                      //lee el boton
  val_int=map(analogRead(A0), 0, 1023, 0, 180);                    //lee el valor del pot1
  val_float =(float)map(analogRead(A1), 0, 1023, 0, 500)*1/100.0;  //lee el valor del pot2

    // Sending Values to ros
  Send_data= "bool=" + (String)val_bool + "/int=" + (String)val_int + "/float=" + (String)val_float;    //Cadena que almacena toda la información
  Send_data.toCharArray(msg,30);      //Guarda y convierte todo en un vector de char de 30 posiciones  
  str_msg.data = msg;                  //Guarda lo que se va a enviar en el topic
  N_Ardu.publish(&str_msg);             //publica el topic
  NodoArduino.spinOnce();              
  delay(100);
}

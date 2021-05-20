# ROS_Project_Publishers-Suscribers

_All the documentation on which this project is based can be found on the ROS website. In this project, the connection of 8 nodes is made in which different types of data are sent between them and subsequently sending and receiving data is generated from an Arduino Uno (9 nodes in total including the one from Arduino). I recommend previously installing Arduino and the arduino ros serial node to be able to work properly_

## Structure - Nodes in Linux

The 9 nodes of this project send, receive and process information, each node script has its comments where the operation of each one is explained. In this way I will only present here a brief description of each node and the execution of the nodes by terminal.

The package contains ROS nodes A through H that publish and subscribe different types of variables, including Bool, Int16, FLoat32, Char, and String. Finally, there is a Node with serial communication between ROS and Ardunio for implementation in the real world.

(H -> ARDUINO, ARDUINO -> A), these ROS nodes are meant to use a fuzzy logic controller to consider 3 signals and make a decision for a final actuator.

* Node A: This node subscribes to a topic string from the Arduino node and splits the received string according to the sensor. Post each value in a different topic: Bool, Int16 and Float32.

* Node B: This node subscribes to a Bool topic of Node A, calculates the low/medium/high level using semi-fuzzy logic. Post a String that contains each of the calculated values.

* Node C: This node subscribes to a topic Int of Node A, calculates the low/medium/high level using semi-fuzzy logic. Post a String that contains each of the calculated values.

* Node D: This node subscribes to a Float topic of Node A, calculates the low/medium/high level using semi-fuzzy logic. Post a String that contains each of the calculated values.

* Node E: This node subscribes to a topic String of Node B, extracts the low/medium/high level and compares its values using semi-fuzzy logic. Finally, it publishes a character by string with the letter with the highest value.

* Node F: This node subscribes to a topic String of Node C, extracts the low/medium/high level and compares its values using semi-fuzzy logic. Finally, it publishes a character by string with the letter with the highest value.

* Node G: This node subscribes to a topic String of Node D, extracts the low/medium/high level and compares its values using semi-fuzzy logic. Finally, it publishes a character by string with the letter with the highest value.

* Node H: This node subscribes to a topic String of Nodes E, F and G, receives the letters according to each node and performs semi-fuzzy logic making a decision as appropriate for the final actuator. Finally, post a single character string containing the decision.

* Arduino Node: This node subscribes to a topic String of Node H, uses the value to configure a position of the servomotor, it also takes the value of 3 sensors and publishes a String with the value of the sensors.


### Execution

_1)To execute the code, you must execute the following in the terminal_

* Roscore is running in the first terminal
```
roscore
```

* In a different terminal for each script the following statement is executed
```
rosrun Carpeta_nodo Nombre_script.py
```

* In a different terminal to view all the nodes and that they are effectively connected, the following sentence is executed
```
rqt_graph
```


### Arduino Node Execution

To run the Arduino node, it is necessary to give permissions to the input port of the card, for this the following is done:

_1) Once the code is ready, the following sentences must be executed in the terminal_
```
sudo chmod 777 /dev/ttyACM0   #The permissions are given to the port (The zero can change this information the delivery of the previous sentence)
```

_2) The code is loaded into the arduino and subsequently the following ROS statements are executed_
```
rosrun rosserial_python serial_node.py /dev/ttyACM0   #In a second terminal this sentence is run (Note: For this to work, the rosserial library must be installed)
```

## Author

* Eymer S. Tapias

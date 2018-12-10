#Server 

#Please run in server_pi folder:
python3 server.py

#The Close/Open Gate Button should light up an LED (no transmitter for a real gate)
#The Server code sets up an MQTT over Websockets connection and tranmits json mqtt messages
#The GUI will change text colors depending on if the gate is open/closed and does not depend on aws to change
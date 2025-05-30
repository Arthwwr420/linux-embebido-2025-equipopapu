#Standard Python libs
import time 
#3rd party libs
import serial
#Local Modules
from serial_device import SerialDevice

SERIAL_PORT = "ttyACM0"
BAUDRATE = 9600

serial_dev = SerialDevice(
    port = SERIAL_PORT,
    baudrate = BAUDRATE
)

time.sleep(2)
message = serial_dev.send_msg("Connect")
# message = serial_dev.readline()

print(type(message))
print(message )

while True: 
    try: 
        to_send = input('Mensaje a enviar: ')
        recieved = serial_dev.send_msg(to_send)
        #recieved = serial_dev.readline()
        print(recieved)
    except KeyboardInterrupt:
        break

serial_dev.disconnect()
print('Listo!')



#Standard Python libs
import time 
#3rd party libs
import serial
#Local Modules

SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 9600

serial_dev = serial.Serial(
    port = SERIAL_PORT,
    baudrate = BAUDRATE
)

time.sleep(2)
serial_dev.write(b"Connect")
message = serial_dev.readline()

print(type(message))
print(message.decode(encoding='utf-8'))

while True: 
    try: 
        to_send = input('Mensaje a enviar: ')
        serial_dev.write(to_send.encode())
        time.sleep(1)
        recieved = serial_dev.readline()
        print(recieved.decode())
    except KeyboardInterrupt:
        break

serial_dev.close()
print('Listo!')



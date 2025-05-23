import os
import sys
import time
import serial

BAUDRATES = [
        4800,
        9600,
        38400,
        460800,
        57600


        ]

class SerialDevice:
    def __init__ (self, port:str,baudrate:int):
        if baudrate not in BAUDRATES:
            raise ValueError(f"Not a Valid Baudrate!(baudrate)")
        port = '/dev/' + port
        if port not in self.find_available_serial_ports():
            raise ValueError("Not a valid Port!{port}")

        self.serial_device=serial.Serial(
                port = port,
                baudrate = baudrate
                )
        time.sleep(2)
        self.serial_device.write(b'Connect')
        time.sleep(1)
        m = self.serial_device.readline()
        print(m.decode())
        m = self.serial_device.readline()
        print(m.decode())

    def send_msg(self, message:str)-> None:
        self.serial_device(message.encode())
        time.sleep(1)
        return self.read_msg()

    def read_msg(self) -> str:
        return self.serial_device.readline().decode()

    def disconnect(self) ->None:
        self.serial_device.close()
    
    @staticmethod
    def find_available_serial_ports() -> list[str]:
        if sys.platform.startswith('darwin'):
            ports = os.listdir('/dev/')
            ports = [port for port in ports if port.startswith('cu.')] 
        elif sys.platform.startswith('linux'):
            ports = os.listdir('/dev/')
            ports = [port for port in ports if port.startswith('tty')] 
        elif sys.platform.startswith('win'):
            ports = [f'COM(i)' for i in range[1, 256] ] 
        else: 
            return None

        return ports
        
#serialses = SerialDevice('ttyACM0',9600)

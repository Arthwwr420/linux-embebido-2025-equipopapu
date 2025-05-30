from tkinter import Button
from tkinter import Frame
from tkinter.ttk import Combobox
from tkinter import Label
from tkinter import Text
from tkinter import END

from SerialDevice.serial_device import SerialDevice
from SerialDevice.serial_device import BAUDRATES
from SerialDevice.caesar import caesar_encrypt, caesar_decrypt

class SerialDevicesBar(Frame):
    def __init__(self, master= None, font :str = "Arial",
                 fsize:int =12, 
                 fcolor:str='BLACK', 
                 *argc:int, 
                 **argv:chr 
                 ):
        super().__init__(master, *argc, **argv)
        self.arduino=None
        self.serial_devices_label = Label(
                self, 
                text='Pick A Serial Port',
                font=[font,fsize],
                foreground=fcolor
                )
        self.serial_devices_combobox = Combobox(
                self, 
                values=SerialDevice.find_available_serial_ports(),
                font=[font,fsize],
                foreground=fcolor
                )
        self.baudrates_combobox = Combobox(
                self, 
                values =BAUDRATES,
                font=[font,fsize],
                foreground=fcolor
                )
        self.caesar_combobox = Combobox(
                self, 
                values = ['Encrypt', 'Decrypt','None'],
                font = [font,fsize],
                foreground = fcolor,
                )
        self.send_msg_label = Label(
                self, 
                text='Send a message to Arduino',
                font=[font,fsize],
                foreground=fcolor
                )
        self.textbox = Text (
                self, 
                font=[font,fsize],
                height=2,
                foreground=fcolor
                )
        self.send_message_button = Button(
                self,
                text='Send Message',
                font=(font, fsize),
                command=self.send_msg,
                foreground=fcolor

                )
        self.recieve_msg_label = Label(
                self, 
                text='Message recieved from Arduino',
                font=[font,fsize],
                foreground=fcolor
                )

        self.textbox_recieve_msg = Text (
                self, 
                font=[font,fsize],
                height=2,
                foreground=fcolor
                )
        self.caesar = 0;
        self.init_gui()


        
    def init_gui(self):
        self.serial_devices_label.pack(side='top', padx=5,pady=5,fill='x')
        self.serial_devices_combobox.pack(side='top',fill='x')
        self.caesar_combobox.pack(side='top', padx=5,pady=5,fill='x')
        self.baudrates_combobox.pack(side='top',fill='x')
        self.send_msg_label.pack(side='top', padx=5,pady=5,fill='x')
        self.textbox.pack(side='top', padx=5,pady=5,fill='x')
        self.send_message_button.pack(side='top', padx=5,pady=5,fill='x')
        self.serial_devices_combobox.current(0)
        self.baudrates_combobox.current(0)
        self.caesar_combobox.current(2)
        self.serial_devices_combobox.bind('<<ComboboxSelected>>',self.connect_arduino) 
        self.baudrates_combobox.bind("<<ComboboxSelected>>",  self.connect_arduino)
        self.caesar_combobox.bind("<<ComboboxSelected>>",  self.set_caesar)
        self.recieve_msg_label.pack(side='top', padx=5,pady=5,fill='x')
        self.textbox_recieve_msg.pack(side='top', padx=5,pady=5,fill='x')


    def get_available_serial_ports(self) -> list[str]:
        port_list = ["port"]
        post_list.extend(SerialDevice.find_available_serial_ports())
        return port_list

    def connect_arduino(self, event):
        print("Looking for Arduino...")
        if self.arduino is None and self.serial_devices_combobox.get() != 'Port:':
            self.arduino = SerialDevice(
                    port = self.serial_devices_combobox.get(),
                    baudrate = int(self.baudrates_combobox.get())
                )
            print('Arduino fonund')
        elif self.serial_devices_combobox.get() != 'Port:':
            self.arduino.diconnect()
            self.arduino = SerialDevice(
                    port = self.serial_devices_combobox.get(),
                    baudrate = int(self.baudrates_combobox.get())
                    )
            print('Arduino fonund')

    def send_msg(self):
        text = self.textbox.get('1.0',"end-1c")
        text = self.caesar_msg(text)
        if self.arduino is not None:
            recieved=self.arduino.send_msg(text)
            recieved = recieved.replace('\r','')
            self.textbox_recieve_msg.insert("1.0",recieved)
        else:
            print("No arduino Found :(")

    def set_caesar(self,event):
        if self.caesar_combobox.get() == 'None':
            self.caesar = 0
        elif self.caesar_combobox.get() == 'Encrypt':
            self.caesar = 1
        else:
            self.caesar = 2

    def caesar_msg(self, text:str):
        if self.caesar == 0:
            return text
        elif self.caesar == 1:
            return caesar_encrypt(text, 4)
        else:
            return caesar_decrypt(text,4)

from tkinter import Tk
from tkinter import Label

import yaml

from SerialDevice.ui.serial_devices_bar import SerialDevicesBar


class MainApp(Tk):
    def __init__(self, *argc, **argv):
        super().__init__(*argc, **argv)
        self.serial_devices_label = Label(
                        self, 
                        text=3
                        )
        self.config = self.loag_config()
        self.title(self.config['main_app']['title'])
        self.serial_devices_bar = SerialDevicesBar(self, 
                                                   self.config['main_app']['font'],
                                                   self.config['main_app']['font_size']
                                                   )
        self.geometry(f"{self.config['main_app']['width']}x{self.config['main_app']['height']}")
        self.init_gui()
    
    def init_gui(self):
        self.serial_devices_bar.pack(side='left',expand=True,fill='both')

    @staticmethod
    def loag_config():
        with open('SerialDevice/config.yaml','r') as f:
            return yaml.safe_load(f)



if __name__ == '__main__':
                      
    print('Main Code Running...')

    app = MainApp()
    app.mainloop()

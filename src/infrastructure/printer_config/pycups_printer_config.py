from src.application.ports.printer_port import PrinterPort
import cups
import os
from dotenv import load_dotenv

load_dotenv()

class PyCupsPrinterConfig(PrinterPort):
    def __init__(self):
        self.printerTarget=os.getenv("PRINTER")
        self.conn= cups.Connection()
        self.opciones = {
        "copies": "1",
        "media": "A4",
        "sides": "one-sided",
        "fit-to-page": "true",
        }
  
    
    def printFile(self,filepath:str):
        impresoras_avilables=self.conn.getPrinters()
        if self.printerTarget not in impresoras_avilables:
            raise Exception("Verique que la impresora este encendida, o que usted este en la red correcta")
  
        self.conn.printFile(self.printerTarget,filepath,filepath,self.opciones)
        print("archivo impreso")
        
        

from src.application.ports.mailer_port import MailerPort
from src.application.ports.printer_port import PrinterPort


class EpsonConnectPrinterConfig(PrinterPort):
    def __init__(self,mailer:MailerPort):
        self.mailer= mailer


    def printFile(self,filepath:str):

        self.mailer.sendMail(filepath)
        
        return 
        


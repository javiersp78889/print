from src.application.ports.mailer_port import MailerPort
import os
import smtplib
from email.message import EmailMessage

class SmtpMailerConfig(MailerPort):

    def __init__(self): 
        #configuracion del cliente de envio
        self.mail=os.getenv("MAIL")
        self.mail_secret= os.getenv("MAIL_SECRET")
        #configuracion del mensaje

    
    def connect(self):
        #configuracion del servidor smtp
        mailer=smtplib.SMTP("smtp.gmail.com",587)
        mailer.starttls()
        mailer.login(self.mail,self.mail_secret)
        return mailer

    def sendMail(self,filepath):
        mailer=self.connect()
        msg= EmailMessage()
        msg["From"]=self.mail
        msg["To"]= os.getenv("MAIL_PRINTER")
        with open(filepath,"rb") as f:
            msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(filepath)
        )
        try:
            mailer.send_message(msg)
        except:
            print("Error al intentar imprimir")
        finally:
            mailer.quit()
    
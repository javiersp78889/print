
from flask import Flask,request,abort
import os
from src.middleware.middleware_auth import Authorization
from src.presentation.printerControllers.printer_controller import PrinterController
from src.presentation.uploadController.uploadController import UploadController
from src.infrastructure.mailer_config.smtplib_mailer_config import SmtpMailerConfig
from src.infrastructure.printer_config.epsonconnect_printer_config import EpsonConnectPrinterConfig
from src.infrastructure.printer_config.pycups_printer_config import PyCupsPrinterConfig
from src.infrastructure.pdfmaker_config.pdf_maker_config import PdfMaker
from src.application.usecases.print_usecase import printUseCase

#validamos que la ruta exista o sino la creamos
os.makedirs("temp",exist_ok=True)
os.makedirs("output",exist_ok=True)


#Configuracion de Flask
app= Flask(__name__,static_folder="temp",static_url_path='/temp')



#instancias de servicios de infrastructura
#generador de pdf
pdfService= PdfMaker()
#servicio de mensajeria
smtpmailer_config=SmtpMailerConfig()
#metodos de impresion
#pyCupsprinterConfig= PyCupsPrinterConfig()
epsonConnectConfig= EpsonConnectPrinterConfig(smtpmailer_config)

#instancias de casos de uso 
printUsecase= printUseCase(pdfService,epsonConnectConfig)

#instancias de controladores
printer_controller= PrinterController(printUsecase)
upload_controller= UploadController()

#instancias de middlewares
middleware= Authorization()

#middleware validate api_key
app.before_request(middleware.authorization)

#ruta para imprimir
app.add_url_rule("/print",view_func=printer_controller.create_impresion,methods=['POST'])

#ruta para subir imagen
app.add_url_rule("/upload",view_func=upload_controller.upload_image, methods=['POST'])
    

if __name__=="__main__":
 app.run(debug=True)

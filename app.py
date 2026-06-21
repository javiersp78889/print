
from flask import Flask,request,abort
import os
from src.infrastructure.removebg.rembg_config import RemoveBG
from src.middleware.middleware_auth import Authorization
from src.presentation.printerControllers.printer_controller import PrinterController
from src.presentation.uploadController.uploadController import UploadController
from src.infrastructure.mailer_config.smtplib_mailer_config import SmtpMailerConfig
from src.infrastructure.printer_config.epsonconnect_printer_config import EpsonConnectPrinterConfig
from src.infrastructure.pdfmaker_config.pdf_maker_config import PdfMaker
from src.application.usecases.print_usecase import printUseCase
from flask_cors import CORS

#validamos que la ruta exista o sino la creamos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMP_DIR = os.path.join(BASE_DIR, "temp")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)


#Configuracion de Flask
app= Flask(__name__,static_folder="temp",static_url_path='/temp')
CORS(app,    resources={r"/*": {"origins": "*"}},allow_headers=["Content-Type", "X-API-Key"])



#instancias de servicios de infrastructura
#Removedor de fondo de imagenes
removeBg=RemoveBG()
#generador de pdf
pdfService= PdfMaker(BASE_DIR)
#servicio de mensajeria
smtpmailer_config=SmtpMailerConfig()
#metodos de impresion
epsonConnectConfig= EpsonConnectPrinterConfig(smtpmailer_config)

#instancias de casos de uso
printUsecase= printUseCase(pdfService,epsonConnectConfig,BASE_DIR)

#instancias de controladores
printer_controller= PrinterController(printUsecase)
upload_controller= UploadController(BASE_DIR,removeBg)

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

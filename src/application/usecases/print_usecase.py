from src.application.ports.pdf_port import PDFPort
from src.application.ports.printer_port import PrinterPort
from src.util.enum.print_enum import PrintType
import os
from threading import Thread




class printUseCase:
    def __init__(self,pdfMake:PDFPort,printer:PrinterPort,BASE_DIR:str):
        self.pdfmake= pdfMake
        self.printer=printer
        self.BASE_DIR=BASE_DIR
        self.temp=os.path.join(self.BASE_DIR,"temp")
    def clean_print(self,path):
        #eliminamos el pdf del output
        try:
            if os.path.exists(path):
                os.unlink(path)
                for n in os.listdir(self.temp):
                    direccion = os.path.join(self.temp,n)
                    os.unlink(direccion)
        except Exception:
            pass

    def worker(self,path):
        try:
            self.printer.printFile(path)
        finally:
            self.clean_print(path=path)

    def execute(self,images:list[str],case:PrintType):
        path=""
        match case:
            case PrintType.ONE_PER_PAGE:
                path=self.pdfmake.onePerPage(image_list=images)
                print("Archivo generado uno por pagina",path)
            case PrintType.TWO_PER_PAGE:
                path= self.pdfmake.twoPerPage(image_list=images)
                print("Archivo generado dos por paginas",path)
            case PrintType.TREE_PER_PAGE:
                path= self.pdfmake.threePerPage(image_list=images)
            case PrintType.TWELF_PER_PAGE:
                path= self.pdfmake.twelfPerPage(image_list=images)
            case _:
                raise Exception ({"message":"Esta opcion no existe"},400)
        #mandamos a imprimir
        Thread(target=self.worker, args=(path,)).start()
        #limpiamos los residuos de la impresion

        return {"message":"Impresora lista para imprimir, espere unos momentos"}

from flask import request

from src.application.usecases.print_usecase import printUseCase
from src.util.types.TprinterDoc import TPrinterDoc
from src.util.enum.print_enum import PrintType


class PrinterController:
    def __init__(self,printusecase:printUseCase):
        self.printusecase=printusecase
    def create_impresion(self):
        data:TPrinterDoc= request.json
        tipo_impresiones=data.get('tipo')
        images_list=data.get("images")
        if not tipo_impresiones:
            return {"error": "tipo es requerido"}, 400
        if not images_list:
            return {"error": "images es requerido"}, 400
        try:
            case= PrintType(tipo_impresiones)
            return self.printusecase.execute(images=images_list,case=case)
        except ValueError:
            return {"error": "el tipo de impresion seleccionado no es válido"}, 400
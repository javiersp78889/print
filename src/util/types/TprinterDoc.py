from typing import TypedDict

from src.util.enum.print_enum import PrintType

class TPrinterDoc(TypedDict):
    images: list[str]
    tipo:PrintType

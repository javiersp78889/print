from abc import ABC, abstractmethod

class PrinterPort(ABC):
    @abstractmethod
    def printFile(self,filepath:str):
        pass
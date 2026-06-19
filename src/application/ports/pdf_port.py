from abc import ABC , abstractmethod

class PDFPort(ABC):
    @abstractmethod
    def onePerPage(self,image_list:list[str]):
        pass
    @abstractmethod
    def twoPerPage(self,image_list:list[str]):
        pass
    @abstractmethod
    def threePerPage(self,image_list:list[str]):
        pass
    @abstractmethod
    def twelfPerPage(self,image_list:list[str]):
        pass
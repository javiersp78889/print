from abc import ABC,abstractmethod

class MailerPort(ABC):

    @abstractmethod
    def sendMail(filepath:str):
        pass

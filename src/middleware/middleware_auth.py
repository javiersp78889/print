import os
from flask import request
from dotenv import load_dotenv

load_dotenv()


class Authorization:
    def __init__(self):
       self.API_KEY=os.getenv("API_KEY")
    
    def validate_apikey(self):
        if not self.API_KEY:
            raise RuntimeError("API_KEY no configurada")

    def authorization(self):
        self.validate_apikey()
        header_apikey=request.headers.get("X-API-key")
        if(header_apikey) != self.API_KEY:
            return {"error":"El apikey no es valido"},401
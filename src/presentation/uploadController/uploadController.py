import os
from flask import request
from PIL import Image
from rembg import remove

from src.infrastructure.removebg.rembg_config import RemoveBG


class UploadController:
    def __init__(self,BASE_DIR,removeBg:RemoveBG):
        self.BASE_DIR=BASE_DIR
        self.removeBg=removeBg



    def upload_image(self):
        image= request.files["image"]
        TEMP_DIR = os.path.join(self.BASE_DIR, "temp")
        filepath=os.path.join(TEMP_DIR,image.filename)
        image.save(filepath)

        #removebg
        self.removeBg.remove(filepath)

        return {"message":{
        "path":filepath
        }}
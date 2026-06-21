import os
from flask import request
from PIL import Image
from rembg import remove


class UploadController:
    def __init__(self,BASE_DIR):
        self.BASE_DIR=BASE_DIR



    def upload_image(self):
        image= request.files["image"]
        TEMP_DIR = os.path.join(self.BASE_DIR, "temp")
        filepath=os.path.join(TEMP_DIR,image.filename)
        image.save(filepath)

        #removebg
        input= Image.open(filepath)
        output=remove(input)
        output.save(filepath,"PNG")

        return {"message":{
        "path":filepath
        }}
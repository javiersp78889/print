import os
from flask import request


class UploadController:
    def __init__(self):
        pass


    def upload_image(self):
        image= request.files["image"]
        filepath=os.path.join('temp',image.filename)
        image.save(filepath)
        return {"message":{
        "path":filepath
        }}
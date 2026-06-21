import os
import requests
from PIL import Image
from io import BytesIO

class RemoveBG:
    def __init__(self):
        self.url = os.getenv('REMOVEBG_API')
        self.api_key = os.getenv('REMOVEBG_API_KEY')

        self.headers = {
            "x-api-key": self.api_key
        }


    def remove(self, imagepath: str):
        files = {
            "image": open(imagepath, "rb")
        }
        response = requests.post(
                self.url,
                headers=self.headers,
                files=files,
                data=self.data
            )

        if response.status_code != 200:
            raise Exception(f"rembg error: {response.status_code} {response.text}")

        output = Image.open(BytesIO(response.content)).convert("RGBA")

        bg = Image.new("RGB", output.size, (255, 255, 255))
        bg.paste(output, mask=output.split()[3])

        bg.save(imagepath)
        return imagepath
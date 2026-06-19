from PIL import Image, ImageOps
import os
from src.application.ports.pdf_port import PDFPort


class PdfMaker(PDFPort):

    A4_LANDSCAPE = (3508, 2480)

    def __init__(self):
        Image.init()
        os.makedirs("output", exist_ok=True)
        self.path = "output/impresiones.pdf"

    def _save_pdf(self, pages):
        if not pages:
            return None

        pages[0].save(
            self.path,
            save_all=True,
            append_images=pages[1:]
        )

        return self.path

    def _multiple_per_page(
        self,
        image_list: list[str],
        images_per_page: int,
        image_size: tuple[int, int],
        positions: list[tuple[int, int]]
    ):
        pages = []

        for i in range(0, len(image_list), images_per_page):

            pagina = Image.new(
                "RGB",
                self.A4_LANDSCAPE,
                "white"
            )

            for offset in range(images_per_page):

                index = i + offset

                if index >= len(image_list):
                    break

                with Image.open(image_list[index]) as img:

                    img = (
                        img
                        .convert("RGB")
                        .resize(image_size)
                    )
                    imagen= ImageOps.mirror(img)

                    pagina.paste(
                        imagen,
                        positions[offset]
                    )

            pages.append(pagina)

        return self._save_pdf(pages)
    
    def onePerPage(self, image_list: list[str]):
        pages = []

        for path in image_list:
            with Image.open(path) as img:
                imagen= ImageOps.mirror(img)
                pages.append(imagen.convert("RGB"))

        return self._save_pdf(pages)
    
    def twoPerPage(self, image_list: list[str]):

        return self._multiple_per_page(
            image_list=image_list,
            images_per_page=2,
            image_size=(1954, 2440),
            positions=[
                (0, 0),
                (1754, 0)
            ]
        )

    def threePerPage(self, image_list: list[str]):
        return self._multiple_per_page(
            image_list=image_list,
            images_per_page=3,
            image_size=(1399, 2440),
            positions=[
                (-170, 0),
                (1020, 0),
                (2220, 0)
            ]
        )
    def twelfPerPage(self, image_list):
        return self._multiple_per_page(
            image_list=image_list,
            images_per_page=12,
            image_size=(800,800),
            positions=[
                (0,0),(784,0),(1568,0),(2352,0),
                (0,800),(784,800),(1568,800),(2352,800),
                (0,1600),(784,1600),(1568,1600),(2352,1600)
            ]
        )
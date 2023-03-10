from pdfrw.toreportlab import makerl
from reportlab.pdfgen import canvas

class PDFWriter:

    __slots__ = (
        '__canvas'
    )

    def __init__(self, path: str):
        self.__canvas = canvas.Canvas(path)

    def doFormXOBJ(self, formXOBJ):
        rlobj = makerl(self.__canvas, formXOBJ)
        self.__canvas.doForm(rlobj)

    def setFillColor(self, r: int, g: int, b: int):
        self.__canvas.setFillColorRGB(r / 255, g / 255, b / 255)

    def setPageSize(self, width: float, height: float):
        self.__canvas.setPageSize((width, height))

    def rect(self, x, y, width, height, stroke=1, fill=0):
        self.__canvas.rect(x, y, width, height, stroke, fill)

    def flush(self):
        self.__canvas.showPage()

    def save(self):
        self.__canvas.save()
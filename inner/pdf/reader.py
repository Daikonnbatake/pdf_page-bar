from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl

class PDFReader:

    __slots__ = (
        '__path',
        '__pdf'
    )

    def __init__(self, path: str):
        self.__path = path
        self.__pdf = PdfReader(path, decompress=False)

    def getPageCount(self) -> int:
        return len(self.__pdf.pages)

    def getPages(self):
        return self.__pdf.pages

    def getPage(self, page: int):
        return self.__pdf.pages[page]

    def getPageSize(self, page: int):
        raw = list(map(float, self.__pdf.pages[page].MediaBox))
        return (raw[2] - raw[0], raw[3] - raw[1])

    def getPageXOBJ(self, page: int):
        return pagexobj(self.getPage(page))
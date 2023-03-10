from inner.dialogs import GetInPath, GetOutPath
from inner.pdf.reader import PDFReader
from inner.pdf.writer import PDFWriter


in_path = GetInPath('PDF', '*.pdf', '%UserProfile%')
out_path = GetOutPath('PDF', '*.pdf', '%UserProfile%')

reader = PDFReader(in_path)
writer = PDFWriter(out_path)

pages = reader.getPages()
page_count = reader.getPageCount()

for i in range(page_count):
    page = reader.getPage(i)
    xobj = reader.getPageXOBJ(i)
    writer.doFormXOBJ(xobj)

    page_width, page_height = reader.getPageSize(i)
    length = (page_width / (page_count-1)) * i

    writer.setPageSize(page_width, page_height)

    writer.setFillColor(88, 88, 88)
    writer.rect(0, 0, page_width, 40, stroke=0, fill=1)

    writer.setFillColor(168, 168, 168)
    writer.rect(0, 0, length, 40, stroke=0, fill=1)

    writer.flush()

writer.save()
from reportlab.pdfgen import canvas
from PyPDF4 import PdfFileReader, PdfFileMerger, PdfFileWriter
import io
#packet = io.BytesIO()
file = 'files/Material/PDF/Basic_App_Dev_Training_V2.3.pdf'
pdf = PdfFileReader(file, 'rb')
x = pdf.getPage(0).mediaBox[-1]
y = pdf.getPage(0).mediaBox[-2]

c = canvas.Canvas('hello.pdf')
c.drawString(200,200, 'Welcome to reportlab!')
c.setPageSize((y,x))
c.save()


watermark = PdfFileReader('hello.pdf', 'rb')
page = watermark.getPage(0)
page.rotateClockwise(90)


writer = PdfFileWriter()
writer.addPage(page)
result = open('result.pdf', 'wb')

writer.write(result)
result.close()

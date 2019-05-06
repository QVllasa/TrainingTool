from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

buffer = BytesIO()

# create a new PDF with Reportlab
p = canvas.Canvas(buffer, pagesize=A4)
p.drawString(100, 100, "holaaaaaaaaaaaa")
p.showPage()
p.save()

#move to the beginning of the StringIO buffer
buffer.seek(0)
newPdf = PdfFileReader(buffer)

#######DEBUG NEW PDF created#############
pdf1 = buffer.getvalue()
open('pdf1.pdf', 'wb').write(pdf1)
#########################################
# read your existing PDF
existingPdf = PdfFileReader(open('plantilla.pdf', 'rb'))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existingPdf.getPage(0)
page.mergePage(newPdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()
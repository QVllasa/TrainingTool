from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, black, blue, red

buffer = BytesIO()
file = open('files/Material/PDF/Basic_App_Dev_Training_V2.3.pdf', 'rb')
pdf = PdfFileReader(file)
x = pdf.getPage(0).mediaBox[-2]
y = pdf.getPage(0).mediaBox[-1]



# create a new PDF with Reportlab
p = canvas.Canvas(buffer)
r = Color(0,0,0, alpha = 0.5)
p.setFont('Helvetica', 75)
p.setFillColor(r)
p.setPageSize((x, y))
#p.saveState()
p.translate(x/2, y/2)
p.rotate(45)
p.drawCentredString(0, 0, "holaaaaaaaaaaaa")
#p.restoreState()
p.showPage() #so anything you draw on the canvas after calling it will go on the next page.
p.save()

#move to the beginning of the StringIO buffer
buffer.seek(0)
newPdf = PdfFileReader(buffer)

#######DEBUG NEW PDF created#############
pdf1 = buffer.getvalue()
open('pdf1.pdf', 'wb').write(pdf1)
#########################################
# read your existing PDF

output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = pdf.getPage(0)
page.mergePage(newPdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()
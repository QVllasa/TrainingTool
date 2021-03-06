from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from compressor import compress
import os

buffer = BytesIO()
file = open('files/Material/PDF/Basic_App_Dev_Training_V2.3.pdf', 'rb')
material = PdfFileReader(file)
x = material.getPage(0).mediaBox[-2]
y = material.getPage(0).mediaBox[-1]

pageNum = material.getNumPages()

p = canvas.Canvas(buffer)
r = Color(0, 0, 0, alpha=0.5)
p.setFont('Helvetica', 75)
p.setFillColor(r)
p.setPageSize((x, y))

p.translate(x / 2, y / 2)
p.rotate(45)
p.drawCentredString(0, 0, "holaaaaaaaaaaaa")

p.showPage()
p.save()
buffer.seek(0)

watermark = PdfFileReader(buffer)
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
count = float(0)
for page in range(pageNum):
    slide = material.getPage(page)
    slide.mergePage(watermark.getPage(0))
    slide.compressContentStreams()
    output.addPage(slide)
    count += float(100)/float(len(range(pageNum)))
    print(round(count))


outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()

compress('output.pdf', 'output_mat.pdf', power=3)
os.remove('output.pdf')

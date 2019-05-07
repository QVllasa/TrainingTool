from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import *
from reportlab.lib.colors import Color
from compressor import compress
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

pdfmetrics.registerFont(TTFont('Siemens Sans03', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans06', 'misc/Siemens_Sans/SISAN06.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans08', 'misc/Siemens_Sans/SISAN08.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans33', 'misc/Siemens_Sans/SISAN33.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans36', 'misc/Siemens_Sans/SISAN36.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans38', 'misc/Siemens_Sans/SISAN38.ttf'))



file = open('files/new_version/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.pdf', 'rb')

buffer = BytesIO()

material = PdfFileReader(file)
# x = material.getPage(0).mediaBox[-2]
# y = material.getPage(0).mediaBox[-1]

pageNum = material.getNumPages()

p = canvas.Canvas(buffer, pagesize=A4)
#r = Color(0, 0, 0)
#r = Color(55, 53, 53)
p.setFont('Siemens Sans06', 10)
p.setFillColorRGB(55/255,53/255,53/255)

width, height = A4
p.setFillColorRGB(1,1,1)

p.rect(1.7*cm,13*cm, 5*cm, 2*cm,stroke=0, fill=1)
p.setFillColorRGB(0,0,0)


p.drawString(1.7*cm, 14.65*cm, "Qendrim")
p.drawString(1.7*cm, 14.225*cm, "Vllasa")

p.setFont('Siemens Sans03', 10)
p.setFillColorRGB(55/255,53/255,53/255)
p.drawString(1.7*cm, 13.54*cm, "Date: 25. - 28.04.2019")
p.drawString(1.7*cm, 13.125*cm, "Place: Karlsruhe, Germany")

p.setFillColorRGB(1,1,1)
p.rect(13.5*cm,4.6*cm, 4*cm, 1*cm,stroke=0, fill=1)
p.setFillColorRGB(55/255,53/255,53/255)
p.drawString(13.925*cm,4.7*cm,"Max Mustermann")


p.showPage()
p.save()
buffer.seek(0)

watermark = PdfFileReader(buffer)
output = PdfFileWriter()

# add the "watermark" (which is the new pdf) on the existing page

for page in range(pageNum):
    slide = material.getPage(page)
    slide.mergePage(watermark.getPage(0))
    slide.compressContentStreams()
    output.addPage(slide)



outputStream = open('output.pdf', 'wb')
output.write(outputStream)
outputStream.close()

compress('output.pdf', 'output_mat.pdf', power=3)
os.remove('output.pdf')

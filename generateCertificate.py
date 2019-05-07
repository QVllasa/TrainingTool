from PyPDF4 import PdfFileWriter, PdfFileReader
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from compressor import compress
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

pdfmetrics.registerFont(TTFont('Siemens Sans03', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans', 'misc/Siemens_Sans/SISAN006.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans', 'misc/Siemens_Sans/SISAN03.ttf'))



file = open('files/new_version/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.pdf', 'rb')

buffer = BytesIO()

material = PdfFileReader(file)
# x = material.getPage(0).mediaBox[-2]
# y = material.getPage(0).mediaBox[-1]

pageNum = material.getNumPages()

p = canvas.Canvas(buffer, pagesize=A4)
#r = Color(0, 0, 0)
#r = Color(55, 53, 53)
p.setFont('Helvetica', 10)
p.setFillColorRGB(55/255,53/255,53/255)

width, height = A4
p.setFillColorRGB(0,0,0)
p.drawString(1.7*cm, 14.65*cm, "<<ParticipantFName>>")
p.drawString(1.7*cm, 14.225*cm, "<<ParticipantLName>>")

p.setFillColorRGB(55/255,53/255,53/255)
p.drawString(1.7*cm, 13.54*cm, "Date: <<Training_Date>>")
p.drawString(1.7*cm, 13.125*cm, "Place: <<TrainingLocation>>")
p.drawString(14*cm,4.7*cm,"<<Trainer>>")


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

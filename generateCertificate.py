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


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.environ.get("_MEIPASS2", os.path.abspath("."))

    return os.path.join(base_path, relative_path)


pdfmetrics.registerFont(TTFont('Siemens Sans03', 'misc/Siemens_Sans/SISAN03.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans06', 'misc/Siemens_Sans/SISAN06.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans08', 'misc/Siemens_Sans/SISAN08.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans33', 'misc/Siemens_Sans/SISAN33.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans36', 'misc/Siemens_Sans/SISAN36.ttf'))
pdfmetrics.registerFont(TTFont('Siemens Sans38', 'misc/Siemens_Sans/SISAN38.ttf'))
# #
# fname = 'Qendrim'
# lname = 'VllasaVllasa Vllasa Vllasa'
# date = '01. - 05.05.2019'
# location = '123456789101,1121314151617181920'
# location2 = 'Karlsruhe, Germany'
#
#
#
# #location = 'Karlsruhe, Germany'
# path = 'files/Certificates/'
#
# filename_Basic = 'MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V3.pdf'  #
# filename_Edge = 'MindSphere_Academy_attendance_certificate_Edge_Analytics_training_V3.pdf'  # not
# filename_Intro = 'MindSphere_Academy_attendance_certificate_Introduction_Training_V3.pdf'  # not
# filename_IntroWeb = 'MindSphere_Academy_attendance_certificate_Introduction_Webinar_V3.pdf'  # not
# filename_API = 'MindSphere_Academy_attendance_certificate_MC_API_training_V3.pdf'  # not
# filename_Device = 'MindSphere_Academy_attendance_certificate_MC_Device_training_V3.pdf'  # not
# filename_Integration = 'MindSphere_Academy_attendance_certificate_MC_Integration_training_V3.pdf'  # not
# filename_IoTExt = 'MindSphere_Academy_attendance_certificate_MC_IoT_Extension_V3.pdf'  # not
# filename_LIB = 'MindSphere_Academy_attendance_certificate_MC_LIB_training_V3.pdf'  #


def generateCertificate(fname, lname, date, location, path, filename, trainer):
    print(fname, lname, date, location, path, filename)
    file = open(path + filename, 'rb')
    buffer = BytesIO()
    material = PdfFileReader(file)
    pageNum = material.getNumPages()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont('Siemens Sans06', 10)
    p.setFillColorRGB(55 / 255, 53 / 255, 53 / 255)
    p.setFillColorRGB(1, 1, 1)
    p.rect(1.7 * cm, 13 * cm, 5 * cm, 2 * cm, stroke=0, fill=1)
    p.setFillColorRGB(0, 0, 0)
    p.drawString(1.7 * cm, 14.65 * cm, fname)
    p.drawString(1.7 * cm, 14.225 * cm, lname)
    p.setFont('Siemens Sans03', 10)
    p.setFillColorRGB(55 / 255, 53 / 255, 53 / 255)
    p.drawString(1.7 * cm, 13.54 * cm, "Date: ")
    p.drawString(3 * cm, 13.54 * cm, date)

    if not location == '':
        p.drawString(1.7 * cm, 13.125 * cm, "Place: ")
        if len(location)>= 19:
            city, country = location.split(',')
            p.drawString(3 * cm, 13.125 * cm, city+',')
            p.drawString(3 * cm, 12.71 * cm, country)
        else:
            p.drawString(3 * cm, 13.125 * cm, location)

    else:
        pass

    p.setFillColorRGB(1, 1, 1)
    p.rect(13.92 * cm, 5 * cm, 4 * cm, 0.5 * cm, stroke=0, fill=1)
    p.setFillColorRGB(55 / 255, 53 / 255, 53 / 255)
    p.drawString(13.9335 * cm, 5.15 * cm, trainer)
    p.showPage()
    p.save()
    buffer.seek(0)
    watermark = PdfFileReader(buffer)
    output = PdfFileWriter()
    for page in range(pageNum):
        slide = material.getPage(page)
        slide.mergePage(watermark.getPage(0))
        slide.compressContentStreams()
        output.addPage(slide)
    print('saving to temp')
    newfile = filename.replace('.pdf', '')
    src = resource_path('temp/cert/')
    name = str(newfile) + '_' +str(fname[0])+str(lname) + '.pdf'
    if not os.path.exists(src):
        os.makedirs(src)
    certificate = src+name
    outputStream = open(certificate, 'wb')
    output.write(outputStream)
    outputStream.close()
    print('process successfull')
    # compress('output.pdf', 'output_mat.pdf', power=3)
    # os.remove('output.pdf')




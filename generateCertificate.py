# import PyPDF4
#
file = open('files/new_version/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.pdf', 'rb')
# pdf = PyPDF4.PdfFileReader(file)
# for page in pdf.pages:
#     print (page.extractText())

from pdfminer3.pdfdocument import PDFDocument
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfparser import PDFParser
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.layout import LAParams, LTTextBox, LTTextLine, LTFigure


def parse_layout(layout):
    """Function to recursively parse the layout tree."""
    for lt_obj in layout:
        print(lt_obj.__class__.__name__)
        print(lt_obj.bbox)
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())
        elif isinstance(lt_obj, LTFigure):
            parse_layout(lt_obj)  # Recursive



parser = PDFParser(file)
doc = PDFDocument(parser)

rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
for page in PDFPage.create_pages(doc):
    interpreter.process_page(page)
    layout = device.get_result()
    parse_layout(layout)


# from PyPDF4 import PdfFileWriter, PdfFileReader
# from io import BytesIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.colors import Color
# from compressor import compress
# import os
#
# buffer = BytesIO()

# material = PdfFileReader(file)
# x = material.getPage(0).mediaBox[-2]
# y = material.getPage(0).mediaBox[-1]
#
# pageNum = material.getNumPages()
#
# p = canvas.Canvas(buffer)
# r = Color(0, 0, 0, alpha=0.5)
# p.setFont('Helvetica', 75)
# p.setFillColor(r)
# p.setPageSize((x, y))
#
# p.translate(float(x) / float(2), float(y) / float(2))
# #p.rotate(45)
# p.drawCentredString(0, 0, "holaaaaaaaaaaaa")
#
# p.showPage()
# p.save()
# buffer.seek(0)
#
# watermark = PdfFileReader(buffer)
# output = PdfFileWriter()
# # add the "watermark" (which is the new pdf) on the existing page
#
# for page in range(pageNum):
#     slide = material.getPage(page)
#     slide.mergePage(watermark.getPage(0))
#     slide.compressContentStreams()
#     output.addPage(slide)
#
#
#
# outputStream = open('output.pdf', 'wb')
# output.write(outputStream)
# outputStream.close()
#
# compress('output.pdf', 'output_mat.pdf', power=3)
# os.remove('output.pdf')

import sys
import os
import comtypes.client

wdFormatPDF = 17

in_file = 'files/new version/Certification/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.docx'
out_file = 'temp/Certification/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.docx'

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()



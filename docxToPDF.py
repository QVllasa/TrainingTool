import os
from win32com import client
import time



# absolute path is needed
# be careful about the slash '', use '//' or '/' or raw string r"..."
in_file = "/files/new_version/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.docx"
out_file = "/files/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.pdf"

# create COM object
word = client.DispatchEx("Word.Application")
# key point 1: make word visible before open a new document
# convert docx file 1 to pdf file 1
doc = word.Documents.Open(in_file)  # open docx file 1
doc.ExportAsFixedFormat(OutputFileName=out_file,
    ExportFormat=17, #17 = PDF output, 18=XPS output
    OpenAfterExport=False,
    OptimizeFor=0,  #0=Print (higher res), 1=Screen (lower res)
    CreateBookmarks=1, #0=No bookmarks, 1=Heading bookmarks only, 2=bookmarks match word bookmarks
    DocStructureTags=True
    );  # conversion
doc.Close()  # close docx file 1
word.Quit()  # close Word Application



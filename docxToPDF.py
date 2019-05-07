import win32compat.client as client


def convert_to_pdf(filepath:str):
    """Save a pdf of a docx file."""
    try:
        word = client.DispatchEx("Word.Application")
        target_path = filepath.replace(".docx", r".pdf")
        word_doc = word.Documents.Open(filepath)
        word_doc.SaveAs(target_path, FileFormat=17)
        word_doc.Close()
    except Exception as e:
            raise e
    finally:
            word.Quit()


convert_to_pdf('files/new version/Certification/MindSphere_Academy_attendance_certificate_Basic_application_Development_training_V2.docx')
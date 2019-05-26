#import win32com.client

def send_mail_via_com(text, subject, recipient, certificatepath, materialpath):

    # o = win32com.client.Dispatch("Outlook.Application")
    #
    #
    # Msg = o.CreateItem(0)
    # Msg.To = recipient
    #
    # Msg.Subject = subject
    # Msg.Body = text
    #
    #
    # Msg.Attachments.Add(certificatepath)
    # Msg.Attachments.Add(materialpath)
    #
    # Msg.Display()
    print('E-Mail Beginn---------------------')
    print(certificatepath)
    print(materialpath)


    print(recipient)
    print(subject)
    print(text)

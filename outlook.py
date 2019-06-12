import win32com.client as wc


def send_mail_via_com(text, subject, recipient, certificatepath, materialpath):

    print('E-Mail Beginn---------------------')
    if not certificatepath=='' and not materialpath=='':
        print(certificatepath)
        print(materialpath)
        o = wc.Dispatch("Outlook.Application")

        Msg = o.CreateItem(0)
        Msg.To = recipient

        Msg.Subject = subject
        Msg.Body = text
        Msg.Attachments.Add(certificatepath)
        Msg.Attachments.Add(materialpath)
        Msg.Display()
    else: print('Attachments not ready')
    #
    # # print(text)
    # #
    # # print(subject)
    #
    # print(recipient)
    #
    # print(certificatepath)
    #
    # print(materialpath)




import pandas as pd


data = pd.read_excel(r'files/testfile_all.xlsx', sheet_name='FY19')
# data = pd.read_excel(
#     r'files/testfile_all.xlsx')  # for an earlier version of Excel, you may need to use the file extension of 'xls'
# df = pd.DataFrame(data, columns=['Training Title',
#     'Training Start','First Name','Last Name','E-Mail Address'])


df = pd.DataFrame(data,
                  columns=['Course title', 'Date of course', 'First Name', 'Last Name',
                           'E-mail address'])

for a,b in df.iterrows():
    if 'Webinar' in b['Course title']:
        print(b['Course title']+'  '+str(b['Date of course']))





#
# df3 = df2[df['Date of course']]
#
# print(df3)

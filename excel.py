import pandas as pd

data = pd.read_excel (r'files/testfile.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
df = pd.DataFrame(data, columns=['Training Title',
    'Training Start','First Name','Last Name','E-Mail Address'])

df2 = df[df['Training Start'] == '2019-04-15 09:00:00']

print(df2)
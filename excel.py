import pandas as pd

data = pd.read_excel (r'files/testfile.xlsx') #for an earlier version of Excel, you may need to use the file extension of 'xls'
df = pd.DataFrame(data, columns=['Training Title',
    'Training Start','First Name','Last Name','E-Mail Address'])

for id, row in df.iterrows():
    print(row)

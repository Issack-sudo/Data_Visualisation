import pandas as pd

ex='C:\\Users\kabui\OneDrive\Desktop\Financial.xlsx'

#Read the entire excel file
df = pd.read_excel(ex,sheet_name=None)
print(df)

#Read each sheet of the finacial fie

df1 = pd.read_excel(ex,sheet_name=(['Sheet1','Sheet2','Sheet3',
                   'Sheet4','Sheet5','Sheet6',
                   'Sheet7','Sheet8','Sheet9',
                   'Sheet10']))

print(df1)

#export every excel sheet to csv

df = pd.read_excel(ex,sheet_name='Sheet1')
df.to_csv('new1.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet2')
df.to_csv('new2.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet3')
df.to_csv('new3.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet4')
df.to_csv('new4.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet5')
df.to_csv('new5.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet6')
df.to_csv('new6.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet7')
df.to_csv('new7.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet8')
df.to_csv('new8.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet9')
df.to_csv('new9.csv',index=False)

df = pd.read_excel(ex,sheet_name='Sheet10')
df.to_csv('new10.csv',index=False)




import pandas as pd

fileName = 'Nilai_KelasA.xlsx'
df = pd.read_excel(fileName, sheet_name='Nilai_KelasA')

print(df.sample(7))
print(df.describe())
print(df.info())
print(df.head(10))
print(df.tail(10))
#df.to_csv('nilaiKuliah2.csv', index=False, sep=';')
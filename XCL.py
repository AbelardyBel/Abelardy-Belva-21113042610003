import openpyxl as pyxl
# Path, Nama file, dan sheet
file_path = "Nilai_KelasA.xlsx"
wb = pyxl.load_workbook(file_path, data_only=True)
sheet = wb ["Nilai_A"]

for row in sheet.iter_rows(min_row=2, max_row=9, min_col=2, max_col=7):
    print([cell.value for cell in row])
    
    listNilai = []

for row in sheet.iter_rows(min_row=15, max_row=20, min_col=2, max_col=7):
    listNilai.append([cell.value for cell in row])

print(listNilai)
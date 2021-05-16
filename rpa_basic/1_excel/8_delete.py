from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.delete_rows(8)
ws.delete_rows(8, 3) # 8번째 줄에서 3줄 삭제

wb.save("sample_delete_row.xlsx")

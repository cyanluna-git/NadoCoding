from openpyxl import Workbook
wb = Workbook() # 새워크북 생성
ws = wb.active # 현재 활설화된 sheet 가져옴
ws.title = "nanoSheet" # sheet 의 이름을 변경
wb.save("sample.xlsx")
wb.close()

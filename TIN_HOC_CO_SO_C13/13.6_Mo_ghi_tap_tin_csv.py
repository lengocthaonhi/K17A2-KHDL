#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 13: Xử lý tập tin trong Python
#Bài 13.6: Mở - đọc - ghi ds vào cuối files csv

import xu_ly_tap_tin

# Nhập tên tập tin và nội dung: # d:\\BT_TinCS\\TIN_HOC_CO_SO_C13\\dienthoai.csv
filename = input("Nhập tên tập tin: ")    
list = [['name','phone'],['Johnny','0989 753951'],['Lucy','0903123456'],['Jack','0913 753951'],['Johnny Lee','0913753852'],['Peter Son','0989 753951'],['Johnnathan','0903 123456']]
# Mở, ghi và đọc tập tin:
xu_ly_tap_tin.write_csv_file(filename, list)

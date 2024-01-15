#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 13: Xử lý tập tin trong Python
#Bài 13.3: Mở - đọc - ghi files

import xu_ly_tap_tin

# Nhập tên tập tin và nội dung: # d:\\BT_TinCS\\TIN_HOC_CO_SO_C13\\Rain.txt
filename = input("Nhập tên tập tin: ")    
content = input("Nhập nội dung: ")
# Mở, ghi tập tin:
xu_ly_tap_tin.write_file(filename,content)

# Đọc kết quả:
xu_ly_tap_tin.read_file(filename)


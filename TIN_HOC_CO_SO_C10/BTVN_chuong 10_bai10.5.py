#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 10: Hàm xử lý number string date time
#Bài 10.5: Kiểm dữ liệu zip code Việt Nam (xem mã có hợp lệ không?)
''' Mã hợp lệ là mã có chính xác 6 chữ số,
tức là chuỗi truyền vào phải thỏa mãn điều kiện:
- chuỗi số phải có 6 số.
- chỉ chứa ký tự số, không có ký tự loại khác'''

def zip_check(chuoi):
    if chuoi.isdigit() == True and len(chuoi) == 6:  # chỉ chứa ký tự số và số lượng các ký tự số này phải = 6
        return "là zip code hợp lệ"
    else:
        return "là zip code KHÔNG hợp lệ"

# gọi hàm
chuoi = input("Nhập chuỗi: ")
print (f"Chuỗi {chuoi}", zip_check(chuoi))

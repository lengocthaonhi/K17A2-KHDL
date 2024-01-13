#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 10: Hàm xử lý number string date time
#Bài 10.8: Xây dựng chương trình xử lý ngày tháng năm
#Xuất ngày theo định dạng: ngày-tháng-năm
# XD chương trình:
# ngày theo định dạng ngày - tháng - năm:
import datetime
def ngay(y,m,d):
    ngay = datetime.date(y,m,d)
    ngay_dinh_dang = ngay.strftime("%d-%m-%y")
    return ngay_dinh_dang
# kiểm tra năm nhuân:
import calendar
def ktra_nhuan(y):
    if calendar.isleap(y) == True:
        return "nhuận"
    else:
        return "không nhuận"

#Cho biết đây là thứ mấy?
def thu(y,m,d):
    if calendar.weekday(y,m,d) == 0:
        return "Thứ Hai"
    elif calendar.weekday(y,m,d) == 1:
        return "Thứ Ba"
    elif calendar.weekday(y,m,d) == 2:
        return "Thứ Tư"
    elif calendar.weekday(y,m,d) == 3:
        return "Thứ Năm"
    elif calendar.weekday(y,m,d) == 4:
        return "Thứ Sáu"
    elif calendar.weekday(y,m,d) == 5:
        return "Thứ Bảy"
    else:
        return "Chủ nhật"

#Cho biết tháng có bao nhiêu ngày
so_ngay = lambda y, m: calendar.monthrange(y,m)

## ----Gọi hàm---

d=int(input("Nhập ngày:"))      # Nhập dữ liệu đầu vào
m=int(input("Nhập tháng:"))
y=int(input("Nhập năm:"))
print("Ngày này viết theo định dạng ngày - tháng - năm là:", ngay(y,m,d))       # In kết quả
print("Năm này là năm:",ktra_nhuan(y))
print("Ngày này rơi vào:",thu(y,m,d))
print(f"Tháng {m} năm {y} có số ngày là", so_ngay(y,m))
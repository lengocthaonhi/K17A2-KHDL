#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 10: Hàm xử lý number string date time
#Bài 10.1: Tìm giá trị lớn nhất, giá trị nhỏ nhất, sử dụng hàm thư viện Numbers:
import numbers
def GT_max(a,b,c):
    GT_max = max(a,b,c)         # hàm tự thiết lập không được trùng tên với các hàm trong thư viện như: max, min, mod, pow, abs, ceil, floor, fabs, round, sqrt ...
    return GT_max

def GT_min(a,b,c):
    GT_min = min(a,b,c)
    return GT_min

# gọi hàm
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
print("Giá trị lớn nhất là:",max(a,b,c))
print("Giá trị nhỏ nhất là:",min(a,b,c))
#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.17: Tìm BCNN của a và b (a và b nhập từ bàn phím)
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
def bscnn(a, b):
    return int(a * b);
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));
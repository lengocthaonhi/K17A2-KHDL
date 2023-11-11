#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.16: Tìm UCLN của a và b (a và b nhập từ bàn phím)
a=int(input("Nhập a:"));
b=int(input("Nhập b:"));
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
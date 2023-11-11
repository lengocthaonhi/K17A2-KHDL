#c, Thuật toán tìm ƯCLN
a = int(input("Nhập a = "));
b = int(input("Nhập b = "));
def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));
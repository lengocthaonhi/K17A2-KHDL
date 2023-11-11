#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT Chương 6
#Bài 1.9:
print("Bài 1.9: Tính tiền lãi và tổng số tiền nhận được")
a=int(input("Số tiền gửi:"))
b=int(input("Số tháng gửi:"))
c=float(input("Lãi suất 1 năm:"))
d=(a*b)*(c/100/12)
print("Tiền lãi=", d)
print("Tiền vốn + lãi=", a, "+", d, "=", a+d)


#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.9: Lambda để tính chu vi, diện tích hình tròn, hình chữ nhật
#Tính diện tích, chu vi hình tròn
import math
# hàm tính diện tích hình tròn:
S_tron = lambda r: math.pow(r,2)*3.14

# hàm tính chu vi hình tròn:
P_tron = lambda r: 2*r*3.14
       
# hàm tính diện tích hình chữ nhật:
S_CN = lambda a,b: a*b

# hàm tính chu vi hình chữ nhật
P_CN = lambda a,b: (a+b)*2


# Gọi hàm:
r=float(input("Nhập bán kính hình tròn r = "))          # Bước 1: Nhập biến
a=float(input("Nhập chiều dài hình chữ nhật a = "))
b=float(input("Nhập chiều rộng hình chữ nhậtb = "))
                                                        # Bước 2: In kết quả (Diễn giải, tên hàm đúng cú pháp --> sẽ trả về kết quả ở return)
print("Diện tích hình tròn S =",S_tron(r))          
print("Chu vi hình tròn C=",P_tron(r))
print("Diện tích hình chữ nhật S=",S_CN(a,b))
print("Chu vi hình chữ nhật P=",P_CN(a,b))



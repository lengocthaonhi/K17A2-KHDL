#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.4: Xây dựng phương thức tính (1)
import math
# def hàm
def f(x,n):
    return math.pow(math.pow(x,2)+1,n)

# gọi hàm
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
print("S =",f(x,n))
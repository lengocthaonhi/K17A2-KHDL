#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.4: Tính diện tích tam giác = công thức Heron
import math
a=float(input("Nhập cạnh a:"))
b=float(input("Nhập cạnh b:"))
c=float(input("Nhập cạnh c:"))
p=((a+b+c)/2)
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là", S)
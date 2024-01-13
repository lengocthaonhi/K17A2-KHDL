#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 10: Hàm xử lý number string date time
#Bài 10.6: Giải phương trình bậc 2: ax^2+bx+c=0
from math import sqrt
import math
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c==0:
            print("Phương trình có 1 nghiệm x = ", -c/b)
else:
    delta=math.pow(b,2)-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm!")
    elif delta==0:
        print("Phương trình có nghiệm kép x = ", -b/(2*a))         
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b-sqrt(delta))/(2*a)))
        print("x2 = ", float((-b+sqrt(delta))/(2*a)))
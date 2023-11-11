#Bài 6: Biểu diễn thuật toán bằng sơ đồ khối và giả mã
#a, Giải hệ phương trình bậc nhất 2 ẩn có dạng
"""ax+by=c 
   dx+ey=f"""
a=int(input("Nhập hệ số a:"))
b=int(input("Nhập hệ số b:"))
c=int(input("Nhập hệ số c:"))
d=int(input("Nhập hệ số d:"))
e=int(input("Nhập hệ số e:"))
f=int(input("Nhập hệ số f:"))
D=a*e-b*d
Dx=c*e-b*f 
Dy=a*f-c*d
if(D!=0):
          print("Hệ có nghiệm x=", Dx/D, "y=", Dy/D)
else:
        if(Dx!=0) or (Dy!=0):
                print("Hệ vô nghiệm")
        else:
                print("Hệ có vô số nghiệm")


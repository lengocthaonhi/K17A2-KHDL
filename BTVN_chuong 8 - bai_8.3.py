#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8:
#Bài 8.3: Viết chương trình để giải phương trình bậc 1 ax+b=0
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
if(a!=0):
          print("Nghiệm x=", -b/a)
elif(a==0) and (b==0):
        print("Phương trình có vô số nghiệm")
else:
        print("Phương trình vô nghiệm")
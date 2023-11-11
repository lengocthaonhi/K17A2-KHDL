#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8:
#Bài 8.13: Tính giá trị biểu thức
n=int(input("Nhập n:"))
A=0
for i in range(1,n+1):
          if i%2!=0:
                  A+=i
print("A=Tổng các số lẻ <=n=", A)
B=0
for i in range(1,n+1):
        if i%2==0:
                B+=i
print("B=Tổng các số chẵn <=n=", B)
C=1
for i in range(1,n+1):
        C*=i
print("C=Tích các số từ 1 đến n=", C)
D=1
for i in range(1,n+1):
        if i%3==0:
                D*=i
print("D=Tích các số chia hết cho 3=", D)
                    
                
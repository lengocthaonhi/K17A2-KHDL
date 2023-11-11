#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.18: Kiểm tra số hoàn hảo
n=int(input("Nhập n:"))
S=0
for i in range(1,n):
          if n%i==0:
                  S+=i
if S==n:
        print("Số hoàn hảo")
else:
        print("Không phải là số hoàn hảo")

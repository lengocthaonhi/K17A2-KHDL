#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.12: Kiểm tra số nguyên tố
x=int(input("Nhập x:"))
for i in range(2,x-1):
          if x%i==0:
                  break
          print("Là hợp số")
else:
        print("Là số nguyên tố")
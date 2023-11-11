#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.5: Kiểm tra năm nhuận
x=int(input("Nhập năm:"))
if(x%400==0):
          print("Là năm nhuận")
elif(x%4==0) and (x%100):
          print("Là năm nhuận")
else:
        print("Là năm không nhuận")


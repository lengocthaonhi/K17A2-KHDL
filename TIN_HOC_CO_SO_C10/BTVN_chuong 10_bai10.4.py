#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 10: Hàm xử lý number string date time
#Bài 10.4: Tính A=(x^2+x+1)+(x^2-x+1)
import math
x=int(input("Nhập x:"))
n=int(input("Nhập n:"))
print("A=",pow((pow(x,2)+x+1),n)+pow((pow(x,2)-x+1),n)) # đã import math rồi nên chỉ cần viết pow thay vì viết đầy đủ math.pow
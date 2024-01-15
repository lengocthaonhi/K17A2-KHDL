#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.7: Viết hàm trả về phần nguyên của hai phép chia số nguyên
#def hàm
def phep_chia_so_nguyen(x,y):
          return(x//y)
#gọi hàm
x=int(input("Nhập x:"))
y=int(input("Nhập y:"))
print(f"Phần nguyên của phép chia {x}/{y} =",phep_chia_so_nguyen(x,y))


          
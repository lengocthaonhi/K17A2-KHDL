#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.6: Viết hàm kiểm tra số nguyên tố
#def hàm
def kiem_tra_so_nguyen_to(n):
    if n<=1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):              
            if n % i==0:
                return False
                break
        return True
# gọi hàm
n=int(input("Nhập n: "))
print(f"{n}",kiem_tra_so_nguyen_to(n))
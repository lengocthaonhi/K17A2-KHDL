#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.1: In ra giá trị theo dấu của 1 số

def sign(x):
    if x<0:
        return -1
    
    elif x>0:
        return 1        
    else:
        return 0
    

# gọi hàm:
x=int(input("Nhập x:"))
print (sign(x))
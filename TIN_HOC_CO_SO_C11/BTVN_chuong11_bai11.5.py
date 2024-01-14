#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.5: List numbers 2
list=[]                          
while True:
        x=input("Nhập giá trị, bấm Enter để dừng lại: ")        
        if x == "":        
                break          
        else:
                x = int(x)      
                list.append(x)
print("list:",list)
#In ra tất cả các số nguyên tố trong list

def kiem_tra_so_nguyen_to(n):           # Bước 1: Nên def hàm kiểm tra số nguyên tố trước (tham khảo bài 9.6)
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

list_NT=[]                              # Bước 2: gọi hàm kiểm tra
for n in list:                         
        NT = kiem_tra_so_nguyen_to(n)
        if NT == True:
                list_NT.append(n)
print ("Các số nguyên tố trong list:",list_NT)

#In các phần tử âm:
list_am=[]
list_duong=[]
for i in list:
        if i<0:
                list_am.append(i)
        elif i>0:                       
                list_duong.append(i)
print("Các phần tử âm trong list:",list_am)
print("TBC âm=",sum(list_am)/len(list_am))
print("Các phần tử dương trong list:",list_duong)
print("TBC dương=",sum(list_duong)/len(list_duong))
print("Giá trị max trong list:",max(list))
print("Giá trị min trong list:",min(list))
list.sort()
print("List sắp tăng dần:",list)


                        
#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.4: List numbers 1
#Tổng list
list=[]
while True:
        x = int(input("Nhập giá trị:")) 
        list.append(x)
        tiep = input("Tiếp tục nhập giá trị? 1: Có, 0: không ")
        if tiep == "0":                
                break
x = x=int(input("Nhập giá trị cần tìm trong list: "))

print("list:",list)
print("Tổng các giá trị trong list:",sum(list))

find = x in list                               
if find ==True:                                 
        print(x,"có xuất hiện trong list")
        print(x,"xuất hiện",list.count(x),"lần trong list")
else: 
        print(x,"không xuất hiện trong list")

if x > max(list):
        print(x,"lớn hơn tất cả các số trong list")
else:
        print (x,"không lớn hơn tất cả các số trong list")
        new_list=[]
        for i in list:
                if i > x:
                        new_list.append(i)
        print("Các số lớn hơn",x,"trong list:",new_list)        

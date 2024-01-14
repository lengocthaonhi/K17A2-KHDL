#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 12: Module và package trong Python
#Bài 12.2: Module 1: Tổ chức và sử dụng module, áp dụng cho BT chương 11
# TẠO HÀM NHÓM LIST

def do_dai_ds(list):
    do_dai = len(list)
    return do_dai


def the_worst_leader(team1,team2,team3):
    teams=[team1,team2,team3]           # Đội tệ nhất là đội cuối cùng trong ds (có index = -1)
    the_worst_team=teams[-1]
    the_worst_leader = the_worst_team[1] # đội trưởng đứng thứ 2 (index = 1)
    return the_worst_leader


def list_of_animal(animals,find):
    KQ_tim = find in animals      
    if KQ_tim == True:             
        return (f"There is {find} in list of animals")
    else:
        return (f"There is not {find} in list of animals")

def list_num_1():
    list=[]
    while True:
            x = int(input("Nhập giá trị:")) 
            list.append(x)
            tiep = input("Tiếp tục nhập giá trị? (y/n) ")
            if tiep == "n" or tiep =="N":                
                break
    x = int(input("Nhập giá trị cần tìm trong list: "))

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

# Xử lý List_num_2 có liên quan đến số nguyên tố --> xử lý trước đk về số nguyên tố:
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

def list_num_2():
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
    if list_am == []:
        TBC_am = 0
    else:
        TBC_am = sum(list_am)/len(list_am)
    if list_duong ==[]:
        TBC_duong = 0
    else:
        TBC_duong = sum(list_duong)/len(list_duong)   
    print("Các phần tử âm trong list:",list_am)
    print("TBC âm=",TBC_am)
    print("Các phần tử dương trong list:",list_duong)
    print("TBC dương=",TBC_duong)
    print("Giá trị max trong list:",max(list))
    print("Giá trị min trong list:",min(list))
    list.sort()
    print("List sắp tăng dần:",list)         


def list_num_3(list_inch):
    #Đổi inch sang mét
    list_meters=[]
    for i in list_inch:
            i=i*0.0254
            list_meters.append(i)
    print("Đối inch sang mét ta được:",list_meters)
    #In ra 3 chiều cao đầu tiên, 3 chiều cao cuối cùng
    list_temp_1=list_inch[:3]
    list_temp_2=list_inch[7:]                               
    print("3 chiều cao đầu tiên là",list_temp_1)
    print("3 chiều cao cuối cùng là",list_temp_2)
    #In ra chiều cao trung bình, chiều cao lớn nhất, chiều cao nhỏ nhất
    m=sum(list_inch)/len(list_inch)
    print('Chiều cao trung bình là:',round(m,2))
    print('Chiều cao lớn nhất là:',max(list_inch))
    print('Chiều cao nhỏ nhất là:',min(list_inch))
    #Sắp xếp list theo thứ tự tăng dần
    list_inch.sort()
    print("Thứ tự tăng dần:",list_inch)
    #Sắp xếp list theo thứ tự giảm dần
    list_inch.sort()
    list_inch.reverse()
    print("Thứ tự giảm dần:",list_inch)

# áp dụng kiến thức Tạo list-comprehension (tạo ra list mói từ 1 list cũ hoặc vòng lặp dạng in-line, kết hợp với các đk cho trước)
def elementwise_greater_than(L, thresh):
    new_list = [True if num > thresh else False for num in L]
    return new_list


def has_lucky_number(nums):
    for num in nums:
        if num%7 != 0:
            continue
        else:
            return True
            break
        
#Bài 11.9: Xác định khách có đến dự tiệc muộn không?
def party_late(arrivals,name):
    if name != arrivals[-1] and arrivals.index(name) > len(arrivals)/2:
        return True
    else:
        return False

#Bài 11.10: Xác định các bữa ăn liên tiếp có nhàm chán không?
def menu_is_boring(meals):
    for i in range(0,len(meals)-1):
        if meals[i] == meals[i+1]:
            return True     
            break      
    else:
        return False



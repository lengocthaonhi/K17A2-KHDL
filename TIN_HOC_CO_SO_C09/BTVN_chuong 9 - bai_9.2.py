#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.2: Tính năm âm lịch (sử dụng hàm)

def can(y):
    can=y%10
    if can==0:
        return "Canh"
    elif can==1:
        return "Tân"
    elif can==2:
        return "Nhâm"
    elif can==3:
        return "Quý"
    elif can==4:
        return "Giáp"
    elif can==5:
         return "Ất"
    elif can==6:
        return "Bính"
    elif can==7:
        can="Đinh"
    elif can==8:
        return "Mậu"
    else:
        return "Kỷ"

def chi(y):
    chi=y%12       
    if chi==0:
        return "Thân"
    elif chi==1:
        return "Dậu"
    elif chi==2:
        return "Tuất"
    elif chi==3:
        return "Hợi"
    elif chi==4:
        return "Tý"
    elif chi==5:
        chi="Sửu"
    elif chi==6:
        return "Dần"
    elif chi==7:
        return "Mão"
    elif chi==8:
        return "Thìn"
    elif chi==9:
        return "Tỵ"
    elif chi==10:
        return "Ngọ"
    else:
        return "Mùi"
    nam_am = can + chi
    return nam_am

# gọi hàm:
y = int(input("Nhập năm:" ))
print(f"Năm {y} lịch âm là năm {can(y)} {chi(y)}")


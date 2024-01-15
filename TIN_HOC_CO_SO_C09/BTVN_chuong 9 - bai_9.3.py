#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.3: Hàm tính chỉ số BMI

def BMI(can_nang, chieu_cao):
        BMI=can_nang/(chieu_cao*chieu_cao)
        if BMI<18.5:
                return "Gầy"
        elif BMI>=18.5 and BMI<=24.9:
                return "Bình thường"
        else:
                return "Thừa cân"
        
# gọi hàm:
can_nang=float(input("Nhập cân nặng (kg):"))
chieu_cao=float(input("Nhập chiều cao (m):"))
print("Chỉ số BMI của bạn:", BMI(can_nang, chieu_cao))
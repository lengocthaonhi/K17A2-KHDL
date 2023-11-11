#Lê Ngọc Thảo Nhi -DHKL17A2HN
#BT chương 8
#Bài 8.8: Tính tiền thuê phòng của resort theo bảng giá cho trước
r=int(input("Nhập mã phòng bạn muốn:"))
n=int(input("Nhập số đêm:"))
#gán đơn giá theo số phòng
if r==1:
        DG=1260000
elif r==2:
        DG=1550000
elif r==3:
        DG=1830000
elif r==4:
        DG=1830000
elif r==5:
        DG=2120000
elif r==6:
        DG=2120000
elif r==7:
        DG=2540000
else:
        DG=4800000
# gán tỷ lệ giảm giá theo số đêm ở:
if n==1:
        CK=0
elif n<=3:
        CK=0.25
else:
        CK=0.3        
T=DG*n*(1-CK)
print(T)
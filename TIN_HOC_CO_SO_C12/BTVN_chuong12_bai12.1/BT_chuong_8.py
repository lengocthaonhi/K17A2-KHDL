
#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 12: Module và package trong Python
#Bài 12.1 - Module 1. Tổ chức và sử dụng Module cho bài tập của chương 8
# GỌI HÀM

import ham_chuong_8
#8.1
print("Bài 8.1 - Tìm giá trị lớn nhất, nhỏ nhất")
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
d=int(input("Nhập d:"))
print("Gia tri lon nhat la:", ham_chuong_8.max(a,b,c,d))
print("Gia tri nho nhat la:", ham_chuong_8.min(a,b,c,d))
print("----------------------------------------------")


#8.2
print("Bài 8.2 - Tìm giá trị tuyệt đối")
x=float(input("Nhap gia tri x:"))
print(f"|{x}| = ", ham_chuong_8.abs(x))
print("----------------------------------------------")

#8.3
print("Bài 8.3 - Giải pt bậc nhất")
a=float(input("Nhap he so a:"))
b=float(input("Nhap he so b:"))
print("Nghiem cua phuong trinh la: ",ham_chuong_8.gpt_bac_nhat(a,b))
print("----------------------------------------------")

#8.4
print("Bài 8.4 - Tính S tam giác")
a=int(input("Nhap a:"))
b=int(input("Nhap b:"))
c=int(input("Nhap c:"))
print("S tam giac = ", ham_chuong_8.dien_tich_tam_giac(a,b,c))
print("----------------------------------------------")

#8.5: Kiểm tra năm nhuận
print("Bài 8.5 - Kiểm tra năm nhuận")
year=int(input("Nhap nam can kiem tra: "))
print(f"Năm {year}", ham_chuong_8.nam_nhuan(year))
print("----------------------------------------------")

#8.6: Tinh cước xe taxi.
print ("Bài 8.6: Tinh cước xe taxi")
loai_xe = int(input("Nhap loai xe 4 cho hoac 7 cho (4,7): "))
quang_duong = float(input("Nhap quang duong (km): "))
thoi_gian_cho = int(input("Nhap thoi gian cho (phut): "))
print(f"Loai xe: {loai_xe} cho")
print(f"Quang duong: {quang_duong} km")
print(f"Thoi gian cho: {thoi_gian_cho} phut")
print(f"Tong tien: {ham_chuong_8.cuoc_taxi(loai_xe,quang_duong,thoi_gian_cho)} VND")
print("----------------------------------------------")

#8.7: Tính tiền điện
print ("Bài 8.7 - Tính tiền điện")
kwh_dien = float(input("Nhap so kWh dien (kWh): "))
print(f"Tong tiẻn dien la: {ham_chuong_8.tien_dien(kwh_dien)}")
print("----------------------------------------------")


#Bài 8.8: Tính tiền thuê phòng của resort
print ("Bài 8.8 - Tính tiền thuê phòng")
m = int(input("Nhap ma phong (1 - 8):"))
so_dem = int(input("Nhap so dem o lai: "))
print("Thành tiền", ham_chuong_8.tien_thue_phong(m,so_dem))
print("----------------------------------------------")

#8.9: Yêu cầu: Xây dựng chương trình Count down.
print("Bài 8.9 - Xây dựng chương trình Count down.")
print("Dãy count-down:",ham_chuong_8.count_down())
print("----------------------------------------------")

#8.10: Tính S
print("Bài 8.10: Tính S")
n = int(input("Nhap so nguyen n: "))
x = float(input("Nhap so thuc x: "))
print(f"S = {ham_chuong_8.tinh_S(n,x)}")
print("----------------------------------------------")

#8.11: Tính A
print("Bài 8.11: Tính A")
n = int(input("Nhap so nguyen n: "))
x = float(input("Nhap so thuc x: "))
print(f"A = {ham_chuong_8.tinh_A(n,x)}")
print("----------------------------------------------")

#8.12: Kiểm tra số nguyên tố
print("Bài 8.12: Ktra số nguyên tố")
x = int(input("Nhap so can kiem tra: "))
print(f"{x} {ham_chuong_8.check_snt(x)}")
print("----------------------------------------------")

#8.13: Tính giá trị biểu thức
print ("Bài 8.13: Tính giá trị biểu thức")
n = int(input("Nhap vao so nguyen duong n: "))
print("A = tổng các số lẻ nhỏ hơn hay bằng n")
print(f"A = {ham_chuong_8.so_le(n)}")

print("B = tổng các số chẵn nhỏ hơn hay bằng n")
print(f"B = {ham_chuong_8.so_chan(n)}")

print("C = tích các số từ 1 đến n")
print(f"B = {ham_chuong_8.tich_1(n)}")

print ("D= tích các số chia hết cho 3 nhỏ hơn hay bằng n")
print(f"D = {ham_chuong_8.tich_2(n)}")

print ("E = tổng các số nguyên tố nhỏ hơn hay bằng n")
print(f"D = {ham_chuong_8.so_nguyen_to(n)}")
     
print("F = tổng chuỗi đan dấu")
print(f"F = {ham_chuong_8.chuoi_dan_dau(n)}")
print("----------------------------------------------")

#8.14.Tính tổng của N số nguyên nhập vào
print ("Bài 8.14.Tính tổng của N số nguyên nhập vào")
n = int(input("Nhap so cac so nguyen can tinh: "))
print("Tong cac so vua nhap:",ham_chuong_8.tong_1(n))
print("----------------------------------------------")


#8.15.Tính tổng của các số nguyên nhập vào, chấm dứt khi nhập số 0
print ("B8.15.Tính tổng của các số nguyên nhập vào, chấm dứt khi nhập số 0")
print("Tong cac so vua nhap:",ham_chuong_8.tong_2())
print("----------------------------------------------")

#8.16: Xây dựng chương trình nhập từ bàn phím 2 số nguyên a, b. Tìm UCLN(a,b).
print ("B8.16: Xây dựng chương trình nhập từ bàn phím 2 số nguyên a, b. Tìm UCLN(a,b)")
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
print("UCLN(a,b) =",ham_chuong_8.UCLN(a,b))
print("----------------------------------------------")

#8.17: Xây dựng chương trình nhập từ bàn phím 2 số nguyên a, b. Tìm BCNN(a,b).
print ("B8.17: Tìm BCNN(a,b)")
a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))
print("BCNN(a,b) =",ham_chuong_8.BCNN(a,b))
print("----------------------------------------------")

#8.18: Kiểm tra số hoàn hảo
print ("B8.18: Kiểm tra số hoàn hảo")
x = int(input("Nhap vao so nguyen duong x: "))
print(x, ham_chuong_8.so_hoan_hao(x))
print("----------------------------------------------")

#8.19: Đảo ngược số
print("B.19 - In dãy đảo ngược")
day_so = input("Nhap vao mot day so bat ky, moi so cach nhau boi dau cach: ")
print("day_so_moi: ",ham_chuong_8.dao_nguoc_so(day_so))
print("----------------------------------------------")

#8.20: Hàm e^x có khai triển Taylor là : 𝒆^𝒙 ≈ 𝟏 + 𝒙 + (𝒙^𝟐)/(𝟐!) + (𝒙^𝟑)/(𝟑!) + ⋯ + (𝒙^𝒏)/(𝒏!)
print("B.20 - In dãy Tay lo của hàm e^x")
x = int(input("Nhap so nguyen x: "))
print(f"e^{x}, {ham_chuong_8.ham_taylor(x)}")
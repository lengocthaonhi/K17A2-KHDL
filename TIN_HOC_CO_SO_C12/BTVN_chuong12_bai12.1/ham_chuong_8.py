#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 12: Module và package trong Python
#Bài 12.1: Module 1: Tổ chức và sử dụng module, áp dụng cho BT chương 8
# TẠO HÀM

#8.1: Tìm số lớn nhất – số nhỏ nhất
def max(a,b,c,d):
      max = a
      if max < b:
            max = b
      if max < c:
            max = c
      if max < d:
            max = d
      return max

def min(a,b,c,d):
      min = a
      if min > b:
            min = b
      if min > c:
            min = c
      if min > d:
            min = d
      return min

#8.2: Tìm |x|
def abs(x):
      if x>=0:
            return x
      else:
            return -x
         
#8.3: Giải phương trình bậc nhất
def gpt_bac_nhat(a,b):
      if a!=0:
            return -b/a
      else:
            if b == 0:
                  return "vo so nghiem"
            else:
                  return "vo nghiem"
          
#8.4: Tính diện tích tam giác
import math
def dien_tich_tam_giac(a,b,c):
      if a <= 0 or b <= 0 or c <=0 or a + b <= c or b + c <= a or a + c <= b:
            return "3 canh vua nhap khong phai la 3 canh cua 1 tam giac"
      else:
            p=(a+b+c)/2
            s=math.sqrt(p*(p-a)*(p-b)*(p-c))
      return s
              
#8.5: Kiểm tra năm nhuận
def nam_nhuan(year):
      if year<1:
            return "Nam khong xac dinh"
      else:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                  return "la nam nhuan"
            else:
                  return "khong phai la nam nhuan"

#8.6: Tinh cước xe taxi.
def cuoc_taxi(loai_xe,quang_duong,thoi_gian_cho):
      if loai_xe != 4 and loai_xe != 7:
            return "Yeu cau nhap 4 hoac 7"
      else:
            if quang_duong <=0:
                  return "Quang duong khong xac dinh"
            else:
                  if thoi_gian_cho < 0:
                        return "Thoi gian cho khong xac dinh"
                  else:
                        tong_tien = 0.0
                        tien_cho = 0.0
                        if thoi_gian_cho > 5:
                              tien_cho = (thoi_gian_cho - 5) * 800
                        if loai_xe == 4:
                              if quang_duong >= 21:
                                    return 11000 + (20 - 0.8)*12100 + (quang_duong - 20) * 10000 + tien_cho
                              elif quang_duong > 0.8:
                                    return 11000 + (quang_duong - 0.8)*12100 + tien_cho
                              else:
                                    return 11000 + tien_cho
                        if loai_xe == 7:
                              if quang_duong >= 21:
                                    return 13000 + (20 - 0.8)*14100 + (quang_duong - 20) * 12000 + tien_cho
                              elif quang_duong > 0.8:
                                    return 13000 + (quang_duong - 0.8)*14100 + tien_cho
                              else:
                                    return 13000 + tien_cho

         

#8.7: Tính tiền điện
def tien_dien(kwh_dien):
      if kwh_dien < 0: 
            return "So kWh khong xac dinh"
      else:
            if kwh_dien >= 401:
                  return 50*1.675 + 50*1734 + 100*2014 + 100*2536 + 100*2834 + (kwh_dien - 400)*2927
            elif kwh_dien >= 301: 
                  return 50*1.675 + 50*1734 + 100*2014 + 100*2536 + (kwh_dien - 300)*2834
            elif kwh_dien >= 201: 
                  return 50*1.675 + 50*1734 + 100*2014 + (kwh_dien - 200)*2536
            elif kwh_dien >= 101: 
                  return 50*1.675 + 50*1734 + (kwh_dien - 100)*2014
            elif kwh_dien >= 51:
                  return 50*1.675 + (kwh_dien - 50)*1734
            else: 
                  return kwh_dien*1.675
           
#Bài 8.8: Tính tiền thuê phòng của resort
def tien_thue_phong(m,so_dem):
      if m > 8 or m < 1:
            print ("Ma phong khong hop le")
      else:
            if so_dem < 1:
                  print ("So dem khong hop le")
            else:
                  if so_dem > 1 and so_dem < 4:
                        giam_gia = 0.25
                  elif so_dem >= 4:
                        giam_gia = 0.3
                  else:
                        giam_gia = 0.0
                  if m == 1:
                        return 1260000*so_dem*(1-giam_gia)
                  elif m == 2:
                        return 1550000*so_dem*(1-giam_gia)
                  elif m == 3:
                        return 1830000*so_dem*(1-giam_gia)
                  elif m == 4:
                        return 1830000*so_dem*(1-giam_gia)
                  elif m == 5:
                        return 2120000*so_dem*(1-giam_gia)
                  elif m == 6:
                        return 2120000*so_dem*(1-giam_gia)
                  elif m == 7:
                        return 2540000*so_dem*(1-giam_gia)
                  else:
                        return 4800000*so_dem*(1-giam_gia)


#8.9: Yêu cầu: Xây dựng chương trình Count down.
def count_down():
      n = int(input("Nhập số nguyên n: "))
      while n > 0:
            print(n)
            n = n - 1
      else:
            print("Start!!")

#8.10: Tính S
def tinh_S(n,x):
      s = (x**2 + 1)**n
      return s

#8.11: Tính A
def tinh_A(n,x):
      A = (x**2 + x + 1)**n + (x**2 - x + 1)**n
      return A

#8.12: Kiểm tra số nguyên tố
def check_snt(x):
      if x < 2:
            return "khong phai so nguyen to"
      else:
            for i in range(2,x):
                  if x%i == 0:
                        return "khong phai so nguyen to"
                        break
            else:
                  return "la so nguyen to"


#8.13: Tính giá trị biểu thức
#A = tổng các số lẻ nhỏ hơn hay bằng n
def so_le(n):
      tong = 0
      for i in range(0, n+1):
            if i%2!=0:
                  tong = tong + i
      return tong

#B = tổng các số chẵn nhỏ hơn hay bằng n
def so_chan(n):
      tong = 0
      for i in range(0, n+1):
            if i%2==0:
                  tong = tong + i
      return tong

#C = tích các số từ 1 đến n
def tich_1(n):
      tich = 1
      for i in range(1, n+1):
            tich = tich*i
      return tich

#D = tích các số chia hết cho 3 nhỏ hơn hay bằng n
def tich_2(n):
      tich = 1
      for i in range(1, n+1):
            if i%3==0:
                  tich = tich*i
      return tich

#E = tổng các số nguyên tố nhỏ hơn hay bằng n
def so_nguyen_to(n):
      tong = 0
      for i in range(2, n+1):
            for j in range(2,i):
                  if i%j == 0:
                        break
            else:
                  tong = tong + i
      return tong

#F = tổng chuỗi đan dấu
def chuoi_dan_dau(n):
      tong = 0.0
      flag = True
      for i in range(1, n+1):
            if flag == True:
                  tong = tong + 1.0/i
                  flag = False
            else:
                  tong = tong - 1.0/i
                  flag = True
      return tong


#8.14.Tính tổng của N số nguyên nhập vào
def tong_1(n):
      if n < 0:
            print("n khong hop le")
      else:
            tong = 0
            for i in range(1,n+1):
                  k = int(input(f"Nhap so nguyen thu {i}: "))
                  tong = tong + k
      return tong

#8.15.Tính tổng của các số nguyên nhập vào, chấm dứt khi nhập số 0
def tong_2():
      tong = 0
      while True:
            n = int(input("Nhap so nguyen: "))
            tong = tong + n
            if n == 0:
                  return tong
                  break
       

#8.16: Xây dựng chương trình nhập từ bàn phím 2 số nguyên a, b. Tìm UCLN(a,b).
def UCLN(a,b):
      if a < 0 or b < 0:
            print("a, b phai lon hon 0")
      min = a
      if min > b:
            min = b
      for i in range(min, 0, -1):
            if a%i == 0 and b%i == 0:
                  UCLN = i
                  break
      return UCLN     



#8.17: Xây dựng chương trình nhập từ bàn phím 2 số nguyên a, b. Tìm BCNN(a,b).
def BCNN(a,b):
      if a < 0 or b < 0:
            print("a, b phai lon hon 0")
      max = a
      if max < b:
            max = b
      while True:
            if max % a == 0 and max % b == 0:
                  BCNN = max
                  break
            max = max + 1
      return BCNN



#8.18: Kiểm tra số hoàn hảo
def so_hoan_hao(x):
      if x < 0:
            print("x phai la so nguyen duong")
      else:
            if x == 0:
                  return "khong phai la so hoan hao"
            tong = 0
            for i in range(1, x):
                        if x%i==0:
                              tong = tong + i
            if tong == x:
                  return "la so hoan hao"
            else:
                  return "khong phai so hoan hao"

#8.19: Đảo ngược số
def dao_nguoc_so(day_so):
      if day_so[0] != "1":
            print("Day so phai bat dau tu so 1")
      else:
            day_so_nguoc = day_so[::-1]
            pos = 0
            count = 0
            day_so_moi = ""
            for i in day_so_nguoc:
                  if i == " ":
                        k = day_so_nguoc[pos - count : pos]
                        k = k[::-1]
                        if int(k) % 2 != 0:
                              day_so_moi = day_so_moi + k + " "
                        count = 0
                  else:
                        count = count + 1
                  pos = pos + 1
            day_so_moi = day_so_moi + "1"
      return day_so_moi



#8.20: Hàm e^x có khai triển Taylor là : 𝒆^𝒙 ≈ 𝟏 + 𝒙 + (𝒙^𝟐)/(𝟐!) + (𝒙^𝟑)/(𝟑!) + ⋯ + (𝒙^𝒏)/(𝒏!)
# Y.c xây dựng ct gần đúng
def ham_taylor(x):
      E=1
      i=1
      dieu_chinh=x/i
      while dieu_chinh >=0.001:     # chấp nhận đến sai số 10^-4
            E=E+dieu_chinh
            i=i+1
            dieu_chinh=dieu_chinh*x/i
      return E


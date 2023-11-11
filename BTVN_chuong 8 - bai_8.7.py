#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.7: Viết chương trình tính tiền điện dành cho hộ gia đình
A=int(input("Nhập số kWh tiêu thụ:"))
if A<=50:
          tien_dien=A*1678
          print("Tiền điện=", tien_dien)
elif 51<=A<=100:
        tien_dien=50*1678+(A-50)*1734
        print("Tiền điện=", tien_dien)
elif 101<=A<=200:
        tien_dien=50*1678+50*1734+(A-100)*2014
        print("Tiền điện=", tien_dien)
elif 201<=A<=300:
        tien_dien=50*1678+50*1734+100*2014+(A-200)*2536
        print("Tiền điện=", tien_dien)
elif 301<=A<=400:
        tien_dien=50*1678+50*1734+100*2014+100*2536+(A-300)*2834
        print("Tiền điện=", tien_dien)
else:
        tien_dien=50*1678+50*1734+100*2014+100*2536+100*2834+(A-400)*2927
        print("Tiền điện=", tien_dien)
        
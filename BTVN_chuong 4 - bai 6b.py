#b, Tính số ngày của một tháng một năm nào đó
m=int(input("Nhập tháng:"))
y=int(input("Nhập năm:"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print("Tháng này có 31 ngày")
elif m==4 or m==6 or m==9 or m==11:
        print("Tháng này có 30 ngày")
else:
        if y%400==0:
                print("Tháng này có 29 ngày")
        elif y%4==0 and y%100!=0:
                print("Tháng này có 29 ngày")
        else:
                print("Tháng này chỉ có 28 ngày")

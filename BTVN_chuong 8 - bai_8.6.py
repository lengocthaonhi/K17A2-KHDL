#Lê Ngọc Thảo Nhi - DHK17A2HN
#BT chương 8
#Bài 8.6: Tính cước taxi theo biểu phí
a=int(input("Loại xe:"))
s=int(input("Số km:"))
t=int(input("Thời gian chờ:"))
if t<=5:
     w=0
else:
     w=(t-5)*800
if a==4:
     if s<=0.8:
          C=11000+w
     elif s<=20:
          C=11000+(s-0.8)*12100+w
     else:
          C=11000+(20-0.8)*12100+(s-20)*10000+w
else:
     if s<=0.8:
          C=13000+w
     elif s<=30:
          C=13000+(s-0.8)*14100+w
     else:
          C=13000+(30-0.8)*14100+(s-30)*12000+w
print("Tiền cước taxi phải trả=", C)
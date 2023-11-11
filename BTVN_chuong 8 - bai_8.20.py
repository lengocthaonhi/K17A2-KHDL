#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 8
#Bài 8.20: Xây dựng chương trình tính gần đúng
x=int(input("Nhập x:"))
S=1
i=1
sai_so=x/i
while sai_so>=0.001:
        S=S+sai_so
        i=i+1
        sai_so=sai_so*x/i
print(S)
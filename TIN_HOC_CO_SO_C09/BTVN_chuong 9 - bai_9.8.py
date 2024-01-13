#Lê Ngọc Thảo Nhi - DHKL17A2
#BT chương 9
#Bài 9.8: Viết hàm kiểm tra 1 số có phải là số hoàn hảo không?
#def hàm
def kiem_tra_so_hoan_hao(n):
        S=0
        for i in range(1,n):
               if n%i==0:
                S+=i
        if S==n:
                return "là số hoàn hảo"
        else:
                return "không phải số hoàn hảo"
#gọi hàm
n=int(input("Nhập n:"))
print (f"{n}", kiem_tra_so_hoan_hao(n))
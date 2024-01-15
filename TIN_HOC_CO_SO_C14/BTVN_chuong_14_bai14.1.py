#Lê Ngọc Thảo Nhi - DHKL17A2HN
# Chương 14: Bắt lỗi và kiểm soát lỗi
def tam_giac(a,b,c):
          assert a.isdigit()==True and b.isdigit()==True and c.isdigit()==True, "a,b hoặc c không phải là kiểu số"
          assert int(a)>0 and int(b)>0 and int(c)>0, "3 cạnh a, b, c phải dương"
          assert int(a)+int(b)>int(c) and int(a)+int(c)>int(b) and int(b)+int(c)>int(a), "Không thỏa mãn điều kiện tồn tại của tam giác"
          return

a=input("Nhập cạnh a:").strip()
b=input("Nhập cạnh b:").strip()
c=input("Nhập cạnh c:").strip()
tam_giac(a,b,c)
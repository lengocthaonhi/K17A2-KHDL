#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.11: Tuple string
# Tạo 1 tuple có 10 phần tử chuỗi bất kỳ:

tuple=('red','green','yellow','blue','black','white','pink','orange','red','blue')
print("Tuple: ",tuple)

# Nhập index dương (0<=index<10), index âm (-1>=index>=-9):
index_duong = int(input("Nhập index dương (0<=index<10): "))
index_am = int(input("Nhập index dương (-1>=index>=-9): " ))

# Nhập chuỗi cần tìm:
s_find = input("Nhập chuỗi cần tìm: ")

# thực thi (nên viết đầy đủ diễn giải)
print(f"Tuple [{index_duong}] = {tuple[index_duong]}")
print(f"Tuple [{index_am}] = {tuple[index_am]}")
print(f"{s_find} xuất hiện trong tuple {tuple.count(s_find)} lần")
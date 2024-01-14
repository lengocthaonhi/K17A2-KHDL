#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 12: Module và package trong Python
#Bài 12.2: Module 1: Tổ chức và sử dụng module, áp dụng cho BT chương 11
# TẠO HÀM NHÓM TUPLE

#Bài 11.11: Tuple string - Xử lý tuple
def xu_ly_tuple_str(tuple):
    # Nhập index dương (0<=index<10), index âm (-1>=index>=-9):
    print("Tuple: ",tuple)
    index_duong = int(input("Nhập index dương (0<=index<10): "))
    index_am = int(input("Nhập index dương (-1>=index>=-9): " ))
    # Nhập chuỗi cần tìm:
    s_find = input("Nhập chuỗi cần tìm: ")
    print(f"Tuple [{index_duong}] = {tuple[index_duong]}")
    print(f"Tuple [{index_am}] = {tuple[index_am]}")
    print(f"{s_find} xuất hiện trong tuple {tuple.count(s_find)} lần")       

#Bài 11.12: Tuple numbers
def xu_ly_tuple_num(tuple_a,tuple_b):
    # a. Tuple c là kết hợp của tuple a và b
    tuple_c=tuple_a + tuple_b
    print("Tuple c:",tuple_c)
    #b. Tuple d từ tuple c với các phần tử được sắp xếp
    #1. Chuyển tuple c sang list để có thể sắp xếp phần tử
    #2. Sắp xếp các phần tử
    #3. Trả về tuple d sau khi sắp xếp
    list_c=list(tuple_c)
    list_c.sort()
    tuple_d=tuple(list_c)
    print("Tuple d:",tuple_d)
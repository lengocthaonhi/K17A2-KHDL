#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.12: Tuple numbers
tuple_a=(3,1,2,4)
tuple_b=(5,7,6,8)
# a. Tuple c là kết hợp của tuple a và b
tuple_c=tuple_a + tuple_b
print("Tuple c:",tuple_c)
#b. Tuple d từ tuple c với các phần tử được sắp xếp
#1. Chuyển tuple c sang list để có thể sắp xếp phần tử
#2. Sắp xếp các phần tử
#3. Trả về tuple d sau khi sắp xếp
list_c=list(tuple_c)
list_c.sort()
print(list_c)
tuple_d=tuple(list_c)
print("Tuple d:",tuple_d)

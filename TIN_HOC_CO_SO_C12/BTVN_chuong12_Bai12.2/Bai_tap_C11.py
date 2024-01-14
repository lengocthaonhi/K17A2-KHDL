#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 12: Module và package trong Python
#Bài 12.2: Module 1: Tổ chức và sử dụng module, áp dụng cho BT chương 11
# GỌI HÀM
# 1. NHÓM HÀM LIST

import ham_list_11

print("Bài 1 - độ dài danh sách")
a=[1,2,3]
b=[1,[2,3]]
c=[]
d=[1,2,3][1:]
list = a
print("Độ dài list a: ",ham_list_11.do_dai_ds(list))
list = b
print("Độ dài list b: ",ham_list_11.do_dai_ds(list))
list = c
print("Độ dài list c: ",ham_list_11.do_dai_ds(list))
list = d
print("Độ dài list d: ",ham_list_11.do_dai_ds(list))
print('-------------------------------------------------')

print("Bài 2 - chọn đội trưởng tệ nhất")
team1 = ['Steven','Neena','Lex','Alexander','Bruce']
team2 = ['David','Jack','Bill','Tom','Mike','Daniel']
team3 = ['Alexander','Adam','Payam','Kevin','Sigal','Mike']
print("Đội trưởng của đội tệ nhất là:",ham_list_11.the_worst_leader(team1,team2,team3))
print('-------------------------------------------------')

print("Bài 3 - Tìm thú trong vườn thú")
animals = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
find = input("I want to find: ")
print (f"List = {animals}")
No_of_animals = len(animals)
print (f"Number of aninals: {No_of_animals}")
print("Kết quả tìm kiếm:",ham_list_11.list_of_animal(animals,find))
print('-------------------------------------------------')

print("Bài 4 - Xử lý list number 1")
ham_list_11.list_num_1()

print('-------------------------------------------------')
print("Bài 5 - Xử lý list number 2")
ham_list_11.list_num_2()
print('-------------------------------------------------')

print("Bài 6 - Xử lý list number 3")
list_inch=[74,74,72,72,73,69,69,71,76,71]
ham_list_11.list_num_3(list_inch)

print('-------------------------------------------------')
print("Bài 7 - Lớn hơn 1 phần tử - dùng list comprehension")

L = [1,2,3,4]
thresh = 2
print(ham_list_11.elementwise_greater_than(L,thresh))

print('-------------------------------------------------')
print("Bài 8 - List chứa số may mắn")
nums = [2,6,7,9]
print (ham_list_11.has_lucky_number(nums))

print('-------------------------------------------------')
print("Bài 9 - Xác định khách có đến dự tiệc muộn không?")
arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
name = "Gilbert"
print(ham_list_11.party_late(arrivals,name))
name = "Ford"
print(ham_list_11.party_late(arrivals,name))
name = "Mona"
print(ham_list_11.party_late(arrivals,name))
name = "May"
print(ham_list_11.party_late(arrivals,name))
name = "Owen"
print(ham_list_11.party_late(arrivals,name))


print('-------------------------------------------------')
print("Bài 10 -  Xác định các bữa ăn liên tiếp có nhàm chán không?")

meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid','Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
meals = meals_1
print(ham_list_11.menu_is_boring(meals))
meals = meals_2
print(ham_list_11.menu_is_boring(meals))

print('=======================================================')

# 2. NHÓM HÀM TUPLE

import ham_tuple_11
print("Bài 11 -  Tuple string - Xử lý tuple")
tuple=('red','green','yellow','blue','black','white','pink','orange','red','blue')
ham_tuple_11.xu_ly_tuple_str(tuple)

print('-------------------------------------------------')
print("Bài 12 -  Tuple numbers - xử lý tuple")
tuple_a=(3,1,2,4)
tuple_b=(5,7,6,8)
# a. Tuple c là kết hợp của tuple a và b
ham_tuple_11.xu_ly_tuple_num(tuple_a,tuple_b)

print('=======================================================')




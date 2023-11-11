#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT Chương 7
#Bài 7.7
x=int(input("Số tiền muốn đổi:"))
so_to_500000=x//500000
so_to_200000=x%500000//200000
so_to_100000=(x%500000%200000)//100000
so_to_50000=((x%500000%200000)%100000)//50000
tien_con_lai=x-(so_to_500000*500000+so_to_200000*200000+so_to_100000*100000+so_to_50000*50000)
print("Số tờ 500000:", so_to_500000)
print("Số tờ 200000:", so_to_200000)
print("Số tờ 100000:", so_to_100000)
print("Số tờ 50000:", so_to_50000)
print("Tiền còn lại:", tien_con_lai)

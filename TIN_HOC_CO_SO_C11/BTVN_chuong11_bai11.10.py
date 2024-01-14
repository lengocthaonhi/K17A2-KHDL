#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.10: Xác định các bữa ăn liên tiếp có nhàm chán không?
def menu_is_boring(meals):
    for i in range(0,len(meals)-1):
        if meals[i] == meals[i+1]:
            return True     
            break      
    else:
        return False  

meals_1 = ['Redneck Ribs', 'Prawn Star', 'San Quentin Squid','Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2 = ['Redneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
print(menu_is_boring(meals_1))
print(menu_is_boring(meals_2))


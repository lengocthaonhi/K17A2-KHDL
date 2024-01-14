#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.3: List of animal
animals = input("Nhập list thú, các phần tử cách nhau bởi dấu Phảy: ")
list_of_animals = animals.split(",")
find = input("I want to find: ")

print (f"List = {list_of_animals}")

No_of_animals = len(list_of_animals)
print (f"Number of aninals: {No_of_animals}")

KQ_tim = find in list_of_animals      
if KQ_tim == True:              
    print (f"There is {find} in list of animals")
else:
     print (f"There is not {find} in list of animals")

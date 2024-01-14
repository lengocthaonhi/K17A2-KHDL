#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.9: Xác định khách có đến dự tiệc muộn không?
def party_late(arrivals,name):
    if name != arrivals[-1] and arrivals.index(name) > len(arrivals)/2:
        return True
    else:
        return False

arrivals=['Adela','Fleda','Owen','May','Mona','Gilbert','Ford']
name = "Gilbert"
print(party_late(arrivals,name))
name = "Ford"
print(party_late(arrivals,name))
name = "Mona"
print(party_late(arrivals,name))
name = "May"
print(party_late(arrivals,name))
name = "Owen"
print(party_late(arrivals,name))

          
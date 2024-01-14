#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.7: Lớn hơn 1 phần tử

# áp dụng kiến thức Tạo list-comprehension (tạo ra list mói từ 1 list cũ hoặc vòng lặp dạng in-line, kết hợp với các đk cho trước)

def elementwise_greater_than(L, thresh):
    new_list = [True if num > thresh else False for num in L]
    return new_list

L = [1,2,3,4]
thresh = 2
print(elementwise_greater_than(L,thresh))

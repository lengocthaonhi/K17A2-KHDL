#Lê Ngọc Thảo Nhi - DHKL17A2HN
#BT chương 11: Kiểu dữ liệu list, tuple, set, dictionary
#Bài 11.8: Xác định trong danh sách các số có chứa "số may mắn" không?

def has_lucky_number(nums):
    for num in nums:
        if num%7 != 0:
            continue
        else:
            return True
            break
        
nums = [2,6,7,9]
print (has_lucky_number(nums))
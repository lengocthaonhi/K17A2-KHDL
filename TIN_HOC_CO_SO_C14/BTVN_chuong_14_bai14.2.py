#Lê Ngọc Thảo Nhi - DHKL17A2HN
# Chương 14: Bắt lỗi và kiểm soát lỗi
# Bài 14.2: Viết CT cho phép người dùng nhập liên tiếp các số nguyên dương
#a. Việc nhập liệu kết thúc bình thường:
def so_nguyen_duong(list_num):
          while True:
                  try:
                          print("Nhập số:\n")
                          so=input("Nhập: ").strip()
                          assert int(so)>0, "Lỗi số âm!"
                    
                  except AssertionError as e:
                          print(e, "Yêu cầu nhập lại!")

                  else:
                          list_num.append(so)
                          
                  finally:
                          print("------------------------")
                          choose = input("Bạn muốn nhập tiếp không? (nhập 0 để kết thúc)").strip()
                          if choose == "0":
                                  break
list_num=[]
so_nguyen_duong(list_num)
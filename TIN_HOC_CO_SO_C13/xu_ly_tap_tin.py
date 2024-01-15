# Lê Ngọc Thảo Nhi - DHKL17A2HN
# Chương 13: Xử lý tập tin
# TẠO HÀM (def)

# Bài 13.1: Mở - đọc - đóng file
import os
import csv

def read_file(filename):                        
    with open(filename,encoding='utf-8') as f:
        r = f.read()
        print("Nội dung tập tin: \n",r)

# Bài 13.2: Mở - đọc - thống kê - đóng file
def read_report_file(filename):            
    with open(filename,encoding='utf-8') as f:
        content = f.read()
        print("Content of file:\n",content)
        print("-----Report: Lines/ Words/ Chars-----")          
    with open(filename,encoding='utf-8') as f:       # đếm dòng nhờ hàm readlines(N): N là số byte
        line_list = f.readlines()              # hàm readlines cho trả về 1 list các dòng
        print("Lines:",len(line_list))         # số dòng chính là độ dài của list các dòng trả về.
    with open(filename,encoding='utf-8') as f:
        chars = f.read()                        # đếm ký tự nhờ hàm read(N): N là số byte
        print("Chars:",len(chars))

# Bài 13.3: Mở - đọc - ghi file (ghi nội dung mới, xóa nội dung cũ)
def write_file(filename,content):
    with open(filename,'w+',encoding='utf-8') as f:
        f.write(content)
        print (f"Đã ghi nội dung vào tập tin {filename}")
        
# Bài 13.4: Mở - đọc - ghi vào cuối file:
def write_end_of_file(filename,content):
    with open(filename,'a+',encoding='utf-8') as f:
        f.write(content)
        f.write("\n")
        print (f"Đã ghi nội dung vào tập tin {filename}")
    while True:
        ask = input("Bạn có muốn tiếp tục ghi nữa không? (1: có / 0: không)")
        if ask == "1":
            add_content = input("Nhập nội dung: ")
            with open(filename,'a+',encoding='utf-8') as f:
                f.write(add_content)
                f.write("\n")
        else:
            print (f"Đã ghi nội dung vào tập tin {filename}")
            read_file(filename)
            break

# Bài 13.5: Mở - đọc file csv: 
def read_file_csv(filename):
    with open(filename,'r') as file:
        csv_read = csv.reader(file)
        for row in csv_read:
            print(row)


# Bài 13.6: Mở - ghi file csv:              
def write_csv_file(filename, list):
    with open(filename ,'w', newline ='', encoding = 'utf-8') as f:                
            for sub_list in list:
                w = csv.writer(f)
                w.writerow(sub_list)
    print(f"Danh sách mới đã được thêm vào file {filename}")
    print ("Nội dung tập tin: ")  
    with open(filename,'r') as file:
        csv_read = csv.reader(file)
        for row in csv_read:
            print(row[0],'\t',row[1])



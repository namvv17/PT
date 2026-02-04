# BTB1

# name = "Nam"
# age = 22
# height = 1.65
# print("Tên tôi là", name)
# print("Tôi", age, "tuổi")
# print("chiều cao của tôi là ",height)

# # Bài 2
# print("Bài 2:")
# name = input("Tên: ...")
# tuổi = input("Tuổi: ...")
# print("===== THÔNG TIN CÁ NHÂN =====")
# print(name)
# print(tuổi)

# BÀI TẬP BÀI 2
# Bài 1: Nhập 2 số nguyên từ bàn phím
# a = int(input("Nhập số nguyên thứ nhất: "))
# b = int(input("Nhập số nguyên thứ hai:  "))

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b) #chia lấy nguyên
# print(a % b)  #chia lấy dư
# print(a ** b) #lũy thừa

# # Bài 2
# name = input("Nhập tên của bạn: ")
# birth_year= int(input("Nhập năm sinh của bạn: "))
# current_year = 2026

# print("xin chào", name, "bạn", current_year - bird_year, "tuổi")
# print("bạn", current_year - bird_year, "tuổi")

# # Bài 3
# length = float(input("Nhập chiều dài hình chữ nhật: "))
# width = float(input("Nhập chiều rộng hình chữ nhật: "))

# print("Diện tích hình chữ nhật là:", length * width)

# BÀI TẬP BÀI 3 (BẮT BUỘC LÀM)
# Bài 1
# number = int(input("Nhập số nguyên: "))

# if int > 0:
#     print("Số dương")
# elif int < 0:
#     print("Số âm")
# else:
#     print("Số 0")

#Bài 2
# age = int(input("Nhập tuổi của bạn: "))
# if age < 18:
#     print("Chưa đủ tuổi")
# else:
#     print("Được phép lái xe")

#Bài 3

# diem = int(input("Nhập điểm của bạn: "))

# if diem >= 8:
#     print("Giỏi")
# elif diem >=6:
#     print("Khá")
# elif diem == 5:
#     print("Trung bình")
# else:
#     print("Yếu")

# BÀI TẬP BÀI 4
# for & white
# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# Bài 1
# Dùng for: In các số từ 1 đến 10

# number = 0
# for number in range(1,11):
#     print(number)

# # Bài 2 Dùng for: In các số lẻ từ 1 đến 20

# for i in range(1, 20, 2):
#     print(i)

# # Bài 3 Dùng while: Nhập số n Tính tổng từ 1 đến n
# n = int(input("Nhập số n: "))
# while n <= 10:
#     print(n)
#     n += 1
# print("total: ",n)

# # Bài 4 Nhập số n, Kiểm tra n có phải số nguyên tố hay không (Gợi ý: dùng for + break)
# n = int(input("Nhập số n: "))
# total = 0
# i = 1

# while i <= n:
#     total += i
#     i += 1

# print("Tổng từ 1 đến", n, "là:", total)

# BÀI 5: LIST (DANH SÁCH) TRONG PYTHON
# DUYỆT LIST BẰNG for

# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num)

# numbers = [1, 2, 3]
# numbers.append(4)  #THÊM PHẦN TỬ
# numbers.remove(2)  #XÓA PHẦN TỬ
# numbers.pop(2)   #XÓA THEO VỊ TRÍ
# print(numbers)

# numbers = [1, 2, 3, 4]
# print(len(numbers))  # độ dài list

# numbers = [3, 7, 2, 9, 5]
# max_number = numbers[0]

# for num in numbers:
#     if num > max_number:
#         max_number = num

# print("Số lớn nhất:", max_number)

# LIST + INPUT (RẤT QUAN TRỌNG)
# numbers = []

# n = int(input("Nhập số phần tử: "))

# for i in range(n):
#     value = int(input("Nhập số: "))
#     numbers.append(value)

# print(numbers)

# BÀI TẬP BÀI 5 (CỐ GẮNG LÀM)
# Bài 1
# list_numbers = [1,2,3,4,5]
# print("Danh sách số đã nhập:", list_numbers)
# print("tổng các số trong list là:", sum(list_numbers))
# print("Số lớn nhất trong list là:", max(list_numbers))
    
# # Bài 2
# n = [1,2,3,4,5,6,7,8,9,10]

# print("Danh sách số đã nhập:", n)

# for num in n:
#     if num % 2 == 0:
#         print("Số chẵn trong list:", num)

# # Bài 3
# scores = [1,2,3,4,5,6,7,8,9,10]

# for num in scores:
#     if num >= 5:
#         print("Điểm >= 5:", num)
#     else:
#         print("Điểm < 5:", num)
    
# BÀI TẬP BÀI 6
# Viết hàm tinh_binh_phuong(n)in ra bình phương của n
def tinh_binh_phuong(n):
    return n ** 2
tinh_binh_phuong(4)
print("Bình phương của 4 là:", tinh_binh_phuong(4))

# Bài 6.2 Viết hàm in_danh_sach(list_so) in ra từng số trong list
def in_danh_sach(list_so):
    for so in list_so:
        print(so)
in_danh_sach([1,2,3,4,5])
# Bài 6.3 Viết hàm dem_so_chan(list_so)trả về số lượng số chẵn trong list
def dem_so_chan(list_so):
    count = 0
    for so in list_so:
        if so % 2 == 0:
            count = 0
            count += 1

dem_so_chan([1,2,3,4,5,6])

# # BÀI TẬP BÀI 6 DICTIONARY
# Bài 7A
# student ={"name": "Nam", "age": "23", "score": "8.6"}
# print(student["name"])
# print(student["age"])
# print(student["score"])
# for key in student:
#     print(key, ":", student[key])
# Bài 7B
months = (1,2,3,4,5,6,7,8,9,10,11,12)
print(months[0])
print(months[11])
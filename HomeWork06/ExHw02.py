# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231,
#  240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]
count = int(input('enter the digit: '))
user_list = [i for i in range(20, count + 1)]
print(user_list)

# def div2021(data:list):
#     res_list = []
#     for i in  range(len(data)):
#         if data[i] % 20 == 0 or data[i] % 21 == 0:
#             res_list.append(data[i])
#     return res_list      


def div_2021_for_filter(el):
    if el % 20 == 0 or el % 21 == 0:
        return True
    else:
        return False

l = list(filter(div_2021_for_filter, user_list))
print(l)   


# for lambda


l_2 = list (filter(lambda x: x % 20 == 0 or x % 21 == 0, user_list))
print(l_2)

    

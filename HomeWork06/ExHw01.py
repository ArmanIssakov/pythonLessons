# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

count = int(input('Enter th digit: '))
user_list = [i for i in sample(range(20), count)]
print(user_list)

res_list = [user_list[i] for i in range(1,count) if user_list[i] > user_list[i-1]]
print(res_list)

# def max_d(data: list):
#     mn=data[0]
#     res_list2 = []
#     for i in range(len(data)):
#         if mn < data[i]:
#             res_list2.append(data[i])
#             mn = data[i]
#         else:
#             mn = data[i]
#     return res_list2


        

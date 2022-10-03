# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def numbersAndSum(num):
    if(num<0):
        return'Error'
    num_list=sample(range(1,num*5),num)   
    print(num_list)
    sumNum = 0
    for i in range(0,len(num_list),2):
        
        sumNum += num_list[i]
    print(sumNum)   

numbersAndSum(int(input('Введите число')))


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import sample


def multSideNum(num):
    if num<0:
        return'error'
    numList=sample(range(1,num*2),num)
    print(f'Рандомный список {numList}')
    if(len(numList)%2!=0):
        a = (len(numList)//2)
        b = numList.pop(a)
    # print(f'Индекс числа который нужно убрать ({a})')
    # print(numList)
    # print(b)  
    j = -1
    mult= 1
    result = [b]
    
    for i in range(len(numList)):
        if i < len(numList)//2:
            mult = numList[i]*numList[j]
            j-=1
            result.insert(i,mult)

    print(result)    



multSideNum(int(input('Введите число: ')))
# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

user_list = list(map(int,input('Знвчения вводить через пробел: ').split()))
with open('uniqueNum', 'w', encoding='utf-8') as uN:
    uN.write(f'{user_list} \n')
    buff_list = []
    for num in user_list:
        if user_list.count(num)>1:
            continue
        else:
            buff_list.append(num)
    uN.write(f'{buff_list}')        
        



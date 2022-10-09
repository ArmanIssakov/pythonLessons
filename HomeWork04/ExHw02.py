# 2. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
def function(n):
    d = 2
    with open("justNumbers.txt", "w", encoding="utf-8") as j_n:
        j_n.write('[')
        while d * d <= n:
            if n % d == 0:
                j_n.write(f'{d}, ')
                n //= d
            else:
                d += 1
        if n > 1:
            j_n.write(f'{n}]')


num=int(input('Введите число: '))
function(num)

    
 
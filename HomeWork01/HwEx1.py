#1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
d = int(input('Введите число: '))
if(d == 6 or d ==7):
    print('yes')
else:
    print('no')    
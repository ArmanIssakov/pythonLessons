# 1. Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
n = float(input('Введите число:'))
i = len(str(n)) - 1
m = int(n*10**i)
s = 0
while(i>0):
    k=m%10
    s+=k
    m=m//10
    i-=1
print(s)    
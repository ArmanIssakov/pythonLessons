# 3. Задайте список из n чисел, заполненный по формуле 
# (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число:'))
num = []
sumA = 0
for i in range(1,n+1):
    a =round((1+1/i)**i)
    num.append(a)
    sumA +=a
print(num)
print()
print(sumA)
    
    
 
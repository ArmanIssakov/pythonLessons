from decimal import ROUND_HALF_UP, Decimal
number = Decimal(input('Введите число: '))
acc = input('Введите точность: ')
number = number.quantize(Decimal(acc), ROUND_HALF_UP)
print(number)
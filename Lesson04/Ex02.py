


from math import sqrt


def sqr_r(a,b,c):
    d=b**2-4*a*c
    with open('sqr.txt', 'a', encoding='utf-8') as myf:
        if (d>0):
            myf.write(f'{(-b+sqrt(d))/(2*a)}')
            myf.write(f'{(-b-sqrt(d))/(2*a)}')
        elif(d==0):
            myf.write(f'{-b/(2*a)}')
        else:
            myf.write('Нет корней')    

for i in range(3):
    sqr_r(int(input('a')),int(input('b')),int(input('c')))


exit()    

НОК
https://zaochnik.com/spravochnik/matematika/delimost/naimenshee-obschee-kratnoe-nok/

gcd


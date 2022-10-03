#02. Задайте список, состоящий из произвольных слов,
# количество задает пользователь.Напишите программу
#, которая определит индекс второго вхождение строки либо 
# сообщит, что ее нет.
from random import choices
from unittest import result

def list_new(n,word):
    new_list = []
    for i in range(n):
        a = choices(word,k=3)
        new_list.append(''.join(a))
    return new_list

     

def search(my_list, key):
    if my_list.count(key) > 1:
        n=my_list.index(key)
        print(my_list.index(key,n+1))
        print('yes')
    else:
        print(-1)    

result=list_new(10,'abc')
print(result)   
search(result,'abc')
# 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.
from random import sample

def my_list(count: int, abc: str = 'абв'):
    words_list = []
    for i in range(count):
        words = sample(abc, 3) # создаст count списков с элементами [а],[б],[в]. В каждом списке будет по 3 элемента
        words_list.append(''.join(words)) # сначала метод join правращает список words в строку, а потом метод append добавляет эту строку в список words_list
        
    return ' '.join(words_list)  # с помощью метода join мы превращаем список с строку

        

a = my_list(5)
print(a)
print(type(a))        

def delete_abc(words: str):
    created_list = words.split()
    finish_list =[]
    for i in range(len(created_list)):
        if created_list[i] != 'абв':
            finish_list.append(created_list[i])
    return ' '.join(finish_list)

b = delete_abc(a)
print(b)

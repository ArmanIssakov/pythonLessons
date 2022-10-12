# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path

def rle_encode(text='text_words.txt', code_text='text_code_words.txt'):
    if path.exists(text) and not path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, 'a') as my_f_2:
            for i in my_f_1:
                my_f_2.write(''.join([f'{len(list(g))}{k}'for k , g in groupby(i)])) # вот это происходит в квадратных скобках 
                                                                                   #[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
                                                                                   # после чего разделенные и сгрупированные элементы превращаются в список
                                                                                   # потом с помощью join этот список превращает в строку
                                                                                     
    else:
        print('Либо нет файла либо уже существует файл, который будет создаваться')            



def rle_decode(text = 'text_code_words.txt'):
    if path.exists(text):
        with open(text) as my_f:
            n = ''
            for k in my_f:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n+=i
                    else:
                        word_nums.append([int(n), i])
                        n = ''
                print(''.join(starmap(lambda x, y: x * y, word_nums)))    
    else:
        print('файл не найден')                    

# def rle_decode(text = 'text_code_words.txt'):
#     if path.exists(name):
#         with open(name) as my_f:
#             for i in my_f:
#                 word_nums = [''.join(g) for k, g in groupby(i.strip(), key=str.isdigit)]
#                 print(''.join([f'{int(word_nums[i]) * word_nums[i+1]}' for i in range(0, len(word_nums),2)]))
rle_encode()
rle_decode()
 # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
 # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D

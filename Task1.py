# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# with open('file.txt', 'w') as f:
#     f.write('wedwefenvknndscns')
from ctypes import resize


with open('file.txt', 'r') as f:    
    str = f.readline().split()
result = list(filter(lambda i: 'abc' not in i, str))
print(result)        
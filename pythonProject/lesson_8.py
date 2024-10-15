# Контекстный менеджер "with", работа с файлами.
# w - write
# a - add
# x - не создаёт файл с одинаковыми названиями

# file = open('new_file.txt', 'w')
# file.write('что нибудь на киррилице (на русском)')
# file.close()

# with open('new_file.txt', 'a') as file:
#     file.write('\nтретья строка'

# with open('other.txt', 'x') as new_file:
#     new_file.write('new data')
from time import sleep
with open('new_file.txt', 'r') as file:
    for i in file.readlines():
        sleep(1)
        print(i, end='')

#file.readline() пропускает строку
#print(file.read())
#print(file.readlines())


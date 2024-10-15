"""Операторы: принадлежности, назначения. Циклыю."""

"""операторы назначения"""

# number = 5
# number +=5
# number -=3
# number **=2
# number *=0.5
# print(number)

"""Операторы принадлежности"""

# word = 'geeks'
# print('g' in word)
# print('g' not in word)
# print('t' in word)
# print('t' not in word)

# counter = 0
# while counter < 100:
#     if counter == 70:
#         print('stop!')
#         break
#     counter += 1
#     if counter % 2 == 0:
#         continue
#     print('GEEKS',counter)


# rounds = 10
# while rounds > 0:
#     temperature = input(f'enter temperature or exit: ({rounds}) ')
#     if temperature.isalpha():
#         if temperature == 'stop':
#             print('cycle stoppaed!')
#             break
#         else:
#             print('Введите только числа или stop!')
#             continue
#     elif temperature.isnumeric() or temperature.startswith('-'):
#         temperature = int(temperature)
#         if temperature >= -40 and temperature <= 0:
#             print('холодно')
#         elif temperature >= 1 and temperature <= 10:
#             print('прохладно')
#         elif temperature >= 11 and temperature <= 25:
#             print('тепло')
#         elif temperature >= 26 and temperature <= 40:
#             print('жарко')
#         else:
#             print(f"несовиестимая с жизнью темпераиура - {temperature}")
#         rounds -=1

#  i - item, iterable, index


word = 'Kyrgyzstan'.upper()
for letter in word:
    if letter == 'S':
        break
    if letter in 'RYSZ':
        continue
    print(letter)



#задание
#Программа знаков зодиака, (ДЗ 2) - (УЛУЧШЕНИЕ)

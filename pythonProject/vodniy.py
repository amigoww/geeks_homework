monday = float(input('Введите расход за понедельник'))
tuesday = float(input('Введите расход за вторник'))
wednesday = float(input('Введите расход за среду'))
thursday = float(input('Введите расход за четверг'))
friday = float(input('Введите расход за пятницу'))
saturday = float(input('Введите расход за субботу'))
sunday = float(input('Введите расход за воскресение'))

sum_ras = monday + tuesday + wednesday + thursday + friday + saturday + sunday

average = sum_ras / 7
average = round(average, 1)

print(f'общая сумма расходов за неделю составил: {sum_ras} \n'
      f'средняя сумма расходов в день составил: {average}')


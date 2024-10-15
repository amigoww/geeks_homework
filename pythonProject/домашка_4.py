mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]

def format_name(name):
    return name.capitalize()[:15]  # Приводим к заглавной букве и ограничиваем до 15 символов

while True:
    print("\nДоступные команды:")
    print("1) Добавить имя")
    print("2) Изменить имя")
    print("3) Удалить имя")
    print("0) Выход")

    command = input("Введите номер команды: ")

    if command == "1":  # Добавление
        name = input("Введите имя ментора: ")
        formatted_name = format_name(name)
        if len(formatted_name) == 0:
            print("Имя не должно быть пустым.")
            continue
        if formatted_name in mentors:
            print("Такое имя уже существует. Попробуйте другое.")
        else:
            mentors.append(formatted_name)
            print(f"Имя '{formatted_name}' добавлено.")

    elif command == "2":  # Изменение
        old_name = input("Введите имя, которое нужно заменить: ")
        formatted_old_name = format_name(old_name)
        if formatted_old_name not in mentors:
            print("Введенного имени нет в списке.")
        else:
            new_name = input("Введите новое имя ментора: ")
            formatted_new_name = format_name(new_name)
            if len(formatted_new_name) == 0:
                print("Новое имя не должно быть пустым.")
                continue
            if formatted_new_name in mentors:
                print("Такое новое имя уже существует. Попробуйте другое.")
            else:
                idx = mentors.index(formatted_old_name)
                mentors[idx] = formatted_new_name
                print(f"Имя '{formatted_old_name}' изменено на '{formatted_new_name}'.")

    elif command == "3":  # Удаление
        print("Выберите способ удаления:")
        print("a) По индексу")
        print("b) По имени")
        choice = input("Введите 'a' или 'b': ")

        if choice == 'a':
            index_str = input("Введите индекс ментора для удаления (начиная с 0): ")
            try:
                index = int(index_str)
                if 0 <= index < len(mentors):
                    removed = mentors.pop(index)
                    print(f"Ментор '{removed}' удалён.")
                else:
                    print("Некорректный индекс.")
            except ValueError:
                print("Введите корректное целое число.")

        elif choice == 'b':
            name = input("Введите имя ментора для удаления: ")
            formatted_name = format_name(name)
            if formatted_name in mentors:
                mentors.remove(formatted_name)
                print(f"Ментор '{formatted_name}' удалён.")
            else:
                print("Введенного имени нет в списке.")

    elif command == "0":  # Выход
        mentors_tuple = tuple(mentors)
        print("Список менторов:", mentors_tuple)
        break

    else:
        print("Некорректная команда. Пожалуйста, попробуйте снова.")
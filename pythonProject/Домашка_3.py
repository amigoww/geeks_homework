while True:
    slovo = input("Введите любое слово (латиницей или кириллицей) или 'выход' для завершения: ")
    if slovo.lower() == 'выход':
        break

    glas = "AEIOUYАЕЁИОУЫЭЮЯaeiouyаеёиоуыэюя"
    sogl = "BCDFGHJKLMNPQRSTVWXZБВГДЖЗЙКЛМНПРСТФХЦЧШЩbcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ"

    glas_count = sum(1 for char in slovo if char in glas)
    sogl_count = sum(1 for char in slovo if char in sogl)
    total_bukvy = len([char for char in slovo if char.isalpha()])  # подсчет всех букв

    glas_percent = (glas_count / total_bukvy) * 100 if total_bukvy else 0.0
    sogl_percent = (sogl_count / total_bukvy) * 100 if total_bukvy else 0.0

    print(f"Слово: {slovo}")
    print(f"Количество букв: {total_bukvy}")
    print(f"Согласных букв: {sogl_count}")
    print(f"Гласных букв: {glas_count}")
    print(f"Гласные/Согласные: {glas_percent:.2f}% / {sogl_percent:.2f}%\n")
# Словарь с флагами стран
country_flags = {
    'kg': {'red', 'yellow'},  # Кыргызстан
    'ru': {'red', 'blue', 'white'},  # Россия
    'kz': {'blue', 'yellow'},  # Казахстан
    'us': {'red', 'blue', 'white'},  # США
    'tr': {'red', 'white'}  # Турция
}

# Запуск цикла
while True:
    user_input = input("Enter the color (or 'q' to quit): ").lower()

    if user_input == 'q':
        print("Program stopped")
        break

    # Разделение ввода на несколько цветов (если нужно)
    input_colors = set(user_input.split())

    # Флаги, которые содержат все введённые цвета
    matched_countries = []

    # Перебор флагов всех стран
    for country, colors in country_flags.items():
        # Если один цвет, просто проверяем наличие
        if input_colors.issubset(colors):
            matched_countries.append(country)

    # Вывод результатов
    if matched_countries:
        print("Страны с такими цветами флага:", " ".join(matched_countries))
    else:
        print("Нет стран с такими цветами флага.")
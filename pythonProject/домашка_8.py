import random


def guess_number():
    low = 1
    high = 100
    attempts = 0
    guesses = []

    print("Загадайте число от 1 до 100 (но не вводите его!).")

    while True:
        attempts += 1
        guess = (low + high) // 2
        guesses.append(guess)

        print(f"Попытка {attempts}: я думаю, это {guess}.")

        answer = input(
            "Ответьте 'да', если угадал, или 'больше', если ваше число больше, или 'меньше', если ваше число меньше: ").lower()

        if answer == "да":
            print(f"Я угадал число {guess} за {attempts} попыток!")
            with open("results.txt", "w") as file:
                file.write(f"Угаданное число: {guess}\n")
                file.write(f"Количество попыток: {attempts}\n")
                file.write(f"Список всех попыток: {guesses}\n")
            break
        elif answer == "больше":
            low = guess + 1
        elif answer == "меньше":
            high = guess - 1
        else:
            print("Некорректный ввод. Пожалуйста, введите 'да', 'больше' или 'меньше'.")


if __name__ == "__main__":
    guess_number()
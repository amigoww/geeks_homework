movies = {
    "Django Unchained": {
        "John": 10,
        "Jack": 9
    },
    "Troy": {}
}


# Функция для добавления фильма
def add_movie(movie_name):
    movie_name = movie_name.title()  # Название с заглавной буквы
    if movie_name in movies:
        print("This movie already exists!")
    else:
        movies[movie_name] = {}
        print("Movie added successfully")


# Функция для добавления рейтинга фильму
def add_rating(movie_name, user_name, rating):
    movie_name = movie_name.title()
    if movie_name not in movies:
        print("This movie doesn't exist")
    else:
        if rating < 1 or rating > 10:
            print("Rating must be between 1 and 10")
        else:
            movies[movie_name][user_name] = rating
            print(f"A rating has been added for {movie_name}: {user_name} rated it {rating}")


# Функция для просмотра рейтингов всех фильмов
def view_ratings():
    for movie, ratings in movies.items():
        if ratings:
            avg_rating = sum(ratings.values()) / len(ratings)
            print(f"{movie} is rated {avg_rating:.1f}")
        else:
            print(f"Rating is not yet available for {movie}")


# Основная программа с бесконечным циклом
def main():
    while True:
        print("\n1. Add Movie\n2. Add Rating\n3. View Ratings\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            movie_name = input("Enter the movie name: ")
            add_movie(movie_name)

        elif choice == '2':
            movie_name = input("Enter the movie name: ")
            user_name = input("Enter your name: ")
            try:
                rating = int(input("Enter the rating (1-10): "))
                add_rating(movie_name, user_name, rating)
            except ValueError:
                print("Invalid rating. Please enter a number from 1 to 10.")

        elif choice == '3':
            view_ratings()

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# Запуск программы
if __name__ == "__main__":
    main()
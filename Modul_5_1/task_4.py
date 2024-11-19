# У вас есть список:
# cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия",
# "пеплум"]
# Вам необходимо:
# преобразовать данный список в множество;
# добавить 2 жанра на ваш выбор (то что вы захотите);
# удалить какой-то из жанров по вашему выбору;
# удалить некий случайный жанр;
# преобразовать множество обратно в список.

cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]
cinema_genres_sets = set(cinema_genres)
# Создаю множество
print(cinema_genres_sets)
# Добавляю 2 жанра боевик и хоррор
cinema_genres_sets.update(["боевик"], ["хоррор"])
print(cinema_genres_sets)
# Удаляю жанр комедия
cinema_genres_sets.remove("комедия")
print(cinema_genres_sets)
# Удаляю случайный жанр
cinema_genres_sets.pop()
print(cinema_genres_sets)
# Возвращаю обратно в список
cinema_genres_list = list(cinema_genres_sets)
print(cinema_genres_list)

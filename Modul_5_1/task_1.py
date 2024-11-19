# Задача 5.1.1
# Создайте любым способом кортеж из следующих жанров
# литературы:
# Роман, Новелла, Фэнтези, Научная Фантастика.
# И второй кортеж из чисел в следующем порядке:
# 3, 7, 9, 1, 6, 8, 2, 5, 4.
# При помощи методов работы с кортежами проведите следующие
# операции:
# узнайте длину обоих кортежей (это количество элементов в них);
# найдите максимальный и минимальный элемент;
# просуммируйте элементы если это возможно;
# отсортируйте элементы по возрастанию и убыванию в
# результате сортировки и последующих операций необходимо
# получить кортеж.
# Помните что кортеж это неизменяемый тип данных, поэтому для
# некоторых операций нужно создавать новый кортеж.


genre_of_literature_tuple = ("Роман", "Новелла", "Фэнтези", "Научная Фантастика")
digits_tuple = (3, 7, 9, 1, 6, 8, 2, 5, 4)
print(f"Кортеж жанров: {genre_of_literature_tuple}")
print(f"Кортеж чисел: {digits_tuple}")
# узнайте длину обоих кортежей (это количество элементов в них);
genre_tuple = len(genre_of_literature_tuple)
digit_tuple = len(digits_tuple)
print(f"Длина кортежа жанров: {genre_tuple}")
print(f"Длина кортежа чисел: {digit_tuple}")
# просуммируйте элементы если это возможно;
digit_tuple_sum = sum(digits_tuple)
print(f"Сумма чисел в кортеже равна: {digit_tuple_sum}")

# найдите максимальный и минимальный элемент;
genre_tuple_min = min(genre_of_literature_tuple)
genre_tuple_max = max(genre_of_literature_tuple)
print(f"Максимальное значение равно: '{genre_tuple_max}', минимальное значение равно: '{genre_tuple_min}'")

digit_tuple_max = max(digits_tuple)
digit_tuple_min = min(digits_tuple)
print(f"Максимальное значение равно: {digit_tuple_max}, минимальное значение равно: {digit_tuple_min}")
# отсортируйте элементы по возрастанию и убыванию в
# результате сортировки и последующих операций необходимо
# получить кортеж.

# Перевожу кортеж в список для работы с сортировкой
genre_tuple_list = list(genre_of_literature_tuple)
# print(type(genre_tuple_list))
# Сортирую списки по возрастанию и  убыванию
genre_tuple_list_sorted = sorted(genre_tuple_list)
genre_tuple_list_revers = sorted(genre_tuple_list, reverse=True)
# Вывожу результаты преобразовывая обратно в кортеж
print(f"Сортировка жанров по возрастанию: {tuple(genre_tuple_list_sorted)}")
print(f"Сортировка жанров по убыванию: {tuple(genre_tuple_list_revers)}")

digits_list = list(digits_tuple)
digits_list_sorted = sorted(digits_list)
digits_list_revers = sorted(digits_list, reverse=True)
print(f"Сортировка чисел по возрастанию: {tuple(digits_list_sorted)}")
print(f"Сортировка чисел по убыванию: {tuple(digits_list_revers)}")

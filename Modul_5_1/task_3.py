# Создайте любым способом множество из десяти вещей, которые вы
# бы взяли на необитаемый остров. Спросите у кого-то из ваших
# близких, какие вещи они взяли бы туда. Выведите на экран
# множество вещей:
# которые бы взяли вы двое;
# которое взяли только вы;
# которое возьмет ваш близкий человек;
# вещи которые есть и у вас и у вашего близкого человека

my_things = {"веревка", "палатка", "зажигалка", "нож", "спальник", "еда", "рыболовные снасти", "одежда", "посуда"}
friend_things = {"палатка", "нож", "зажигалка", "спальник", "одежда", "посуда", "ружье", "патроны", "топор", "дневник"}
print(f"Мои вещи: {my_things}")
print(f"Вещи друга: {friend_things}")
print()
# Вывожу вещи которые есть у меня и у друга
all_things = my_things.union(friend_things)
print(f"Вещи которые есть у меня и у друга: {all_things}")
print()
# Вывожу вещи которые есть только у меня
unique_my_things = my_things - friend_things
print(f"Вещи которые есть только у меня: {unique_my_things}")
print()
# Вывожу вещи которые есть только у друга
unique_friend_things = friend_things - my_things
print(f"Вещи которые есть только у друга: {unique_friend_things}")
print()
# вывожу вещи которые есть у нас обоих
common_things = my_things & friend_things
print(f"Вещи которые есть у нас обоих: {common_things}")
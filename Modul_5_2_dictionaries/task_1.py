# Задание 5.1
# Необходимо написать приложение для проверки знания английского
# языка, которое по выбору пользователя выставляет один из 3-х уровней
# сложности:
# легкий
# средний
# тяжелый
# В случае если пользователь не выбрал ничего или ввел что-то не
# понятное, то уровень по умолчанию устанавливается – легкий (не
# забудьте сделать обработку ввода на регистр и пробелы).
# Приложение хранит русские и английские слова и предлагает нам
# угадывать. Чтобы нам было проще, программа выдает подсказки с
# длиной слова и первой буквой.
# Основные объекты:
# words_easy, words_medium, words_hard словари формата {“слово”: “перевод”, ….};
# words – словарь формата {“слово”: “перевод”, ….};
# levels – ранги пользователя в зависимости от успехов;
# answers – словарь с записями о верных и неверных ответах;

words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}
words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}
words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
words = (words_easy, words_medium, words_hard)

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}
true_answer = []
false_answer = []
answer = {}
counter = 0

print("Проверим уровень знания английского языка!!!")
print()
choice_difficult = input("Выберите уровень сложности. 'Легкий', 'Средний', 'Сложный': ").title().strip()
if choice_difficult == "Средний":
    words = words_medium
    for key, value in words.items():
        question = input(f"{key.title()}, {len(value)} букв, начинается на '{value[0].title()}...' ").strip()
        if question.title() == value.title():
            counter += 1
            answer[f"{key.title()}"] = "True"
            true_answer.append(f"{key.title()}")
            print(f"Верно. {key.title()} - это {value.title()}. Вы заработали {counter} балл")
        else:
            answer[f"{key.title()}"] = "False"
            false_answer.append(f"{key.title()}")
            print(f"Неверно. {key.title()} - это {value.title()}")
elif choice_difficult == "Сложный":
    words = words_hard
    for key, value in words.items():
        question = input(f"{key.title()}, {len(value)} букв, начинается на '{value[0].title()}...' ").strip()
        if question.title() == value.title():
            counter += 1
            answer[f"{key.title()}"] = "True"
            true_answer.append(f"{key.title()}")
            print(f"Верно. {key.title()} - это {value.title()}. Вы заработали {counter} балл")
        else:
            answer[f"{key.title()}"] = "False"
            false_answer.append(f"{key.title()}")
            print(f"Неверно. {key.title()} - это {value.title()}")
else:
    choice_difficult = "Легкий"
    words = words_easy
    for key, value in words.items():
        question = input(f"{key.title()}, {len(value)} букв, начинается на '{value[0].title()}...' ").strip()
        if question.title() == value.title():
            counter += 1
            answer[f"{key.title()}"] = "True"
            true_answer.append(f"{key.title()}")
            print(f"Верно. {key.title()} - это {value.title()}. Вы заработали {counter} балл")
        else:
            answer[f"{key.title()}"] = "False"
            false_answer.append(f"{key.title()}")
            print(f"Неверно. {key.title()} - это {value.title()}")

level = levels.get(counter)
print()
# Возможно не правильно понял Шаг 2, надо ли выводить answer в терминал?,
# В любом случае она в программе сохраняется в виде словаря.
for key, value in answer.items():
    print(f'"{key}":, {value},')
print()
print("Правильно отвечены слова:")
for item in true_answer:
    print(item)
print()
print("Неправильно отвечены слова:")
for item in false_answer:
    print(item)
print()
print(f"Ваш уровень английского по уровню {choice_difficult} - '{level}'")

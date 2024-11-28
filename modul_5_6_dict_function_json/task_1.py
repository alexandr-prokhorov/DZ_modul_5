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
words = {
    "легкий": words_easy,
    "средний": words_medium,
    "сложный": words_hard
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}


def get_user_level(user_input):
    return words.get(user_input, words_easy)


def base_program(word_dict):
    answers = {}
    for key, value in word_dict.items():
        question = input(f"{key.title()}, {len(value)} букв, начинается на '{value[0].title()}...'").strip()
        answers[key] = question.lower() == value.lower()
    return answers


def get_result(answers, level_dict):
    true_answers = [key for key, value in answers.items() if value]
    false_answers = [key for key, value in answers.items() if not value]

    print("Правильно отвечены слова:")
    print(" ".join(true_answers) if true_answers else "Нет правильных ответов.")

    print("Неправильно отвечены слова:")
    print(" ".join(false_answers) if false_answers else "Нет ошибок.")

    level = level_dict.get(len(true_answers), "нулевой")
    return level

print("Проведем проверку знаний английского языка!")
user_lvl = input("Выберите уровень сложности \nлегкий, средний, сложный.\n").lower()
test_words = get_user_level(user_lvl)
test_answers = base_program(test_words)
result = get_result(test_answers, levels)
print(f"Ваш уровень знаний: {result}")

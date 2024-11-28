import json


def get_user_level(user_input, words_file):
    with open(words_file, 'r', encoding='utf-8') as file:
        words = json.load(file)
    return words.get(user_input, words.get("легкий"))


def base_program(word_dict):
    answers = {}
    for key, value in word_dict.items():
        question = input(f"{key.title()}, {len(value)} букв, начинается на '{value[0].title()}...' ").strip()
        answers[key] = question.lower() == value.lower()
    return answers


def get_result(answers, level_dict):
    true_answers = [key for key, value in answers.items() if value]
    false_answers = [key for key, value in answers.items() if not value]

    print("Правильно отвечены слова:")
    print(" ".join(true_answers) if true_answers else "Нет правильных ответов.")

    print("Неправильно отвечены слова:")
    print(" ".join(false_answers) if false_answers else "Нет ошибок.")

    level = level_dict.get(len(true_answers), "Нулевой")
    return level


def save_results(username, answers, result, file_path):
    data = {
        "username": username,
        "answers": answers,
        "result": result
    }
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

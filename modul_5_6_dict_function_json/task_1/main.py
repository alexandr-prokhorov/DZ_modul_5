import os
from functions import get_user_level, base_program, get_result, save_results

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}
print("Проведем проверку знаний английского языка!")

username = input("Введите ваше имя: ").strip()
user_lvl = input("Выберите уровень сложности (легкий, средний, сложный): ").lower()

words_file = "words.json"

test_words = get_user_level(user_lvl, words_file)

test_answers = base_program(test_words)

result = get_result(test_answers, levels)

results_dir = "results"
os.makedirs(results_dir, exist_ok=True)
result_file = os.path.join(results_dir, f"{username}_result.json")
save_results(username, test_answers, result, result_file)

print(f"\nВаш уровень знаний: {result}")
print(f"Результаты сохранены в файле: {result_file}")

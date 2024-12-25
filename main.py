import random

def randomize_links_from_file(file_path):
    """
    Читает ссылки из файла, перемешивает их в случайном порядке без повторений.

    :param file_path: путь к файлу с ссылками
    :return: список ссылок в случайном порядке
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]
        random.shuffle(links)
        return links
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []

# Путь к файлу с ссылками
file_path = 'links.txt'

# Перемешиваем ссылки из файла
randomized_links = randomize_links_from_file(file_path)

# Выводим результат
if randomized_links:
    print("Ссылки в случайном порядке:")
    for link in randomized_links:
        print(link)
else:
    print("Нет ссылок для обработки.")

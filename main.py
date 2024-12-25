import random

def randomize_links_from_file(file_path, output_file):
    """
    Читает ссылки из файла, перемешивает их и записывает в другой файл в формате одной строки.

    :param file_path: путь к файлу с ссылками
    :param output_file: путь к файлу для записи результата
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            links = [line.strip() for line in file if line.strip()]
        random.shuffle(links)
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(", ".join(links))
        print(f"Результат записан в файл {output_file}")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")

# Путь к входному файлу с ссылками
file_path = 'links.txt'
# Путь к выходному файлу с результатом
output_file = 'result.txt'

# Перемешиваем ссылки и записываем результат
randomize_links_from_file(file_path, output_file)

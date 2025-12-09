from pathlib import Path
import sys
import os
import argparse

def tokenize(text):
    import re
    text = text.casefold().strip()
    text = re.sub(r'[^0-9ёa-zA-Zа-яА-Я-]', ' ', text)
    text = text.replace('ё', 'е')
    text = text.split()
    text = ' '.join(text)
    return text.split(' ')

def count_freq(words):
    unique_words = set(words)
    sorted_unique = sorted(unique_words)
    frequency_dict = {}
    for word in sorted_unique:
        frequency_dict[word] = words.count(word)
    return frequency_dict

def show_statistics(filename, limit):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        tokens = sorted(tokenize(content))
        frequencies = count_freq(tokens)
        top_words = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)[:limit]
    print(top_words)    
    
def display_file_content(filename, show_numbers=False):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_number_width = len(str(len(lines)))
        for index, line in enumerate(lines, start=1):
            if show_numbers:
                print(f"{index}. {line}", end='')
            else:
                print(line, end='')                

def process_arguments():
    parser = argparse.ArgumentParser(description='Утилита для работы с текстовыми файлами')
    parser.add_argument('--mode', type=str, required=True,
                     choices=['stats', 'cat'],
                     help='Режим работы: stats - статистика, cat - просмотр файла')
    parser.add_argument('--input', type=str, required=True,
                     help='Путь к входному файлу')
    parser.add_argument('--output', type=str,
                     help='Путь для сохранения результата (опционально)')
    parser.add_argument('--encoding', type=str, default='utf-8',
                     help='Кодировка файла (по умолчанию: utf-8)')
    parser.add_argument('-t', '--top', type=int,
                     help='Количество наиболее частых слов для вывода (только для режима stats)')
    parser.add_argument('-n', '--number', action='store_true',
                     help='Показывать номера строк (только для режима cat)')
    args = parser.parse_args()
    
    if args.mode == 'stats':
        if not args.top:
            print("Ошибка: для режима stats необходимо указать параметр --top")
            sys.exit(1)
        show_statistics(args.input, args.top)
    elif args.mode == 'cat':
        display_file_content(args.input, args.number)

if __name__ == '__main__':
    process_arguments()

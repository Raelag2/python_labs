import sys
import os
from pathlib import Path

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

path_in = "././data/lab04/input.txt"
if Path(path_in).exists(): # Проверяем наличие входного файла
    with open(path_in, mode="r", newline='', encoding='utf-8') as f:
        stroka = f.read()
        format_stroka = top_n(count_freq(tokenize(stroka)), 5)
        i = write_csv(format_stroka, ('src/lab04/report.csv'), ('word','count'))
        r = read_text('src/lab04/report.csv', encoding = "utf-8")   
        print(r)
else:
    raise FileNotFoundError # Если файла нет - ошибка
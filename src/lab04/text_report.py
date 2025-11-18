import sys
import os
from pathlib import Path

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

path_in = "././data/lab04/input.txt"
path_out = "././src/lab04/report.csv"
if path_in.endswith('.txt'):
    if path_out.endswith('.csv'):
        stroka = read_text(path=path_in)
        stroka = top_n(count_freq(tokenize(stroka)), 5)
        write_csv(stroka, path=path_out, header = ('word','count'))
else:
    raise TypeError
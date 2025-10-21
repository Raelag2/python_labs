import sys
import os
from pathlib import Path

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.lib.text import normalize, tokenize, count_freq, top_n

full_text = Path('././data/lab04/input.txt')
with open(full_text, 'r', encoding='utf-8') as f:
    content = f.read()
    
string = top_n(tokenize(full_text), 5)
print(string)



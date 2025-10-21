import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.lib.text import normalize, tokenize, count_freq, top_n

words = sys.stdin.read()

count_words = (count_freq(tokenize(words)))
top_words =  top_n(tokenize(words), 5)

print("Всего слов: " + str(len(tokenize(words))))
print("Уникальных слов: " + str(len(count_words)))
print("Топ 5:")
for i in range(len(top_words)):
    print(str(top_words[i][0]) + ":" + str(top_words[i][1]))

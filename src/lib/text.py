from re import *
from collections import Counter

def normalize(stroka):
    stroka = stroka.casefold()
    stroka = stroka.replace("ё", "е")
    stroka = stroka.split()
    stroka = " ".join(stroka)
    return stroka

def tokenize(stroka):
    stroka = normalize(stroka)
    pattern = r'\w+(?:-\w+)*'
    match = findall(pattern, stroka)
    return match

def count_freq(stroka):
    freq = Counter(stroka)
    freq = dict(freq)
    return(freq)

def top_n(stroka, n):
    freq = Counter(stroka)
    sorted_freq = sorted(freq.items(), key = lambda item: (-item[1], item[0]))
    return sorted_freq[0:n]

'''stroka = "ПрИвЕт\nМИр\t"
print(normalize(stroka)) '''

'''stroka = "hello,world!!!"
print(tokenize(stroka))'''

'''stroka = ["aa","bb","aa","cc","bb"]
print(count_freq(stroka))'''

'''stroka = (["a","b","a","c","b","a"])
print(top_n(stroka, n=2))'''

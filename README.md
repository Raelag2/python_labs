## Лабораторная работа 1

### Задание 1
```python
name = str(input('Имя: '))
age = int(input('Возраст: '))
print("Привет,", name + '!', 'Через год тебе будет', age + 1)
```
![Картинка 1](./images/lab01/01_greetingsc.png)

### Задание 2
```python
num1 = float(input('a: ').replace(',', '.'))
num2 = float(input('b: ').replace(',', '.'))
summa = num1 + num2
srednee = (num1 + num2) / 2
print('sum='+ str(summa), 'avg=' + str(srednee))
```
![Картинка 2](./images/lab01/02_sum_avg.png)

### Задание 3
```python
price = int(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
print('База после скидки:' + str(base) + ' ₽')
print('НДС:' + str(base * (vat/100)) + ' ₽')
print('Итого к оплате:' + str(base + vat_amount) + ' ₽')
```
![Картинка 3](./images/lab01/03_discount_vat.png)

### Задание 4
```python
minutes = int(input('Минуты: '))
a = minutes // 60
b = minutes - a*60
print(f'{a}:{b:02d}')
```
![Картинка 4](./images/lab01/04_minutes_to_hhmm.png)

### Задание 5
```python
fio = str(input('ФИО: '))
lenfio = len(fio.replace(' ', ''))
fio = fio.split()
f = fio[0][0]
i = fio[1][0]
o = fio[2][0]
print('Инициалы:', str(f) + str(i) + str(o))
print('Длина (символов):', lenfio + 2)
```
![Картинка 5](./images/lab01/05_initials_and_len.png)

### Задание 6
```python
n = int(input())
ochnoe = 0
zaochnoe = 0
for i in range(n):
    info = str(input())
    info = info.split()
    if info.count("True") >= 1:
        ochnoe += 1
    else:
        zaochnoe += 1
print("out:", ochnoe, zaochnoe)
```
![Картинка 6](./images/lab01/06.png)

### Задание 7
```python
trash = str(input())
word= ''
counter = -1
trash = list(trash)
for i in trash:
    counter += 1
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        word += i
        break
trash = trash[counter:]
counter = -1
for j in trash:
    counter += 1
    if j in "0123456789":
        word += trash[counter + 1]
        break
trash = trash[::counter + 1]
trash = "".join(trash)
print(trash)

```
![Картинка 7](./images/lab01/07.png)

## Лабораторная работа 2

### Задание 1
```python
def min_max(numlist):
    max_num = max(numlist)
    min_num = min(numlist)
    min_max = (min_num, max_num)
    return min_max

def unique_sorted(numlist):
    sort_num_list = sorted(set(numlist))
    return sort_num_list

def flatten(tuple_num_list):
    massiv_num_list = []
    for numlist in tuple_num_list:
        if isinstance(numlist, (list, tuple)):
            for num in numlist:
                massiv_num_list.append(num)
        else:
            raise TypeError
    return massiv_num_list

n1 = [3, -1, 5, 5, 0]
n2 = [1.0, 1, 2.5, 2.5, 0]
n3 = [[1], [], [2, 3]]

print(min_max(n1))
print(unique_sorted(n2))
print(flatten(n3))
```
![Вывод результатов всех трех функций](./images/lab02/image1.png)

### Задание 2
```python
def transpose(numlist):
    final_result = []
    for num in range(len(numlist) - 1):
        if len(numlist[num]) != len(numlist[num + 1]):
            raise ValueError
    if numlist == []:
        return []
    cols = len(numlist)
    rows = len(numlist[0])
    for i in range(rows):
        inter_result = []
        for j in range(cols):
            inter_result.append(numlist[j][i])
        final_result.append(inter_result)
    return final_result

def unique_sorted(numlist):
    final_result = []
    for num in range(len(numlist) - 1):
        if len(numlist[num]) == len(numlist[num + 1]):
            final_result.append(sum(numlist[num]))
        else:
            raise ValueError
    final_result.append(sum(numlist[-1]))
    return final_result

def col_sums(numlist):
    final_result = []
    alt_final_result = []
    if len(numlist) == 1:
        alt_final_result.append(numlist[0][0])
        return alt_final_result
    else:
        for num in range(len(numlist) - 1):
            if len(numlist[num]) == len(numlist[num + 1]):
                for i in range(len(numlist[0])):
                    final_result.append(numlist[num][i] + numlist[num + 1][i])
            else:
                raise ValueError
        return final_result

n1 = [[1, 2], [3, 4]]
n2 = [[1, 2, 3], [4, 5, 6]]
n3 = [[1, 2, 3], [4, 5, 6]]

print(transpose(n1))
print(unique_sorted(n2))
print(col_sums(n3))
```
![Вывод результатов всех трех функций](./images/lab02/image2.png)

### Задание 3
```python
def format_record(info):
    fio = info[0]
    group = info[1]
    gpa = info[2]
    fio = fio.split()
    if len(fio) == 3:
        fio[0] = fio[0][0].upper() + fio[0][1:] 
        fio[1] = fio[1][0].upper() + '.'
        fio[2] = fio[2][0].upper() + '.'
        fio = " ".join(fio)
    else: 
        fio[0] = fio[0][0].upper() + fio[0][1:] 
        fio[1] = fio[1][0].upper() + '.'
        fio = " ".join(fio)
    group = 'гр. ' + group
    gpa = "GPA " + str(round(gpa, 2)) + '0'
    return str(fio + ", " + group + ", " + gpa)

info = ("Петров Пётр", "IKBO-12", 5.0)
info2 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(format_record(info))
print(format_record(info2))
```
![Вывод на двух разных входах](./images/lab02/image3.png)

## Лабораторная работа 3
### text из lib
```python
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

```

### text_stats
```python
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
```

![Картинка](./images/lab03/image.png)

## Лабораторная работа 4
### io_txt_csv.py
```python
from pathlib import *
import csv
from typing import Iterable, Sequence

def read_text (path: str, encoding = "utf-8") -> str:
    if type(path) == str:
        if not Path(path).exists():
            raise FileNotFoundError
        if encoding != "utf-8":
            raise UnicodeDecodeError
    else:
        raise TypeError
    return Path(path).read_text(encoding=encoding)

def write_csv(rows, path: str | Path, header: tuple[str, ...] | None) -> None:  
    if rows is None:
        rows = []
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        for j in range(len(rows) - 1): # Проверяем длину каждого элемента данных
            if len(rows[j]) != len(rows[j+1]):
                raise ValueError
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        if header is not None and rows != []:
            if len(header) != len(rows[0]): #заголовков надо столько-же
                raise ValueError
        for r in rows:
            w.writerow(r)
```
### Созданный файл с текстом
![Картинка](./images/lab04/1.png)

### text_report.py
```python
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
```
### Созданный файл csv
![Картинка](./images/lab04/2.png)

## Лабораторная работа 5
### json_csv.py
```python
from pathlib import Path
import json
import csv

def csv_2_json(samples: str, out: str|Path = None, encoding='utf-8'):
    spisok = []
    with open(samples, encoding='utf-8') as csv_fi:
        filtr = csv.DictReader(csv_fi)
        for li1 in filtr:
            spisok.append(li1)
    
    if out is None:
        samples = Path(samples)
        diroput = Path('data\out')
        out = diroput / f'people_from_csv.json'

    with open(out,'w',encoding='utf-8') as json_fi:
        json.dump(spisok, json_fi, ensure_ascii=False)


def json_2_csv(samples: str, out: str|Path = None, encoding = 'utf-8'):
    with open(samples, 'r', encoding='utf-8') as json_fi:
        filtr = json.load(json_fi)
    
    if out is None:
        samples = Path(samples)
        diroput = Path('data\out')
        out = diroput / f'people_from_json.csv'

    with open(out,'w',encoding='utf-8',newline='') as csv_fi:
        head = filtr[0].keys()
        pisa = csv.DictWriter(csv_fi, fieldnames=head)
        pisa.writeheader()
        pisa.writerows(filtr)
 ```

 ### csv_xlsx.py
```python
from pathlib import Path
from openpyxl import *
import csv 

def csv_2_xlsx(samples: str, out: str|Path = None, encoding='utf-8'):
    f_xlsx = Workbook()
    stranica = f_xlsx.active
    stranica.title = 'Эксель формат'

    if out is None:
        samples = Path(samples)
        diroput = Path('data\out')
        out = diroput / f'people.xlsx'

    with open(samples,'r',encoding='utf-8') as csv_fi:
        filtr = csv.reader(csv_fi)
        for nu_st, lin in enumerate(filtr,1):
            for nu_cmn, val in enumerate(lin,1):
                stranica.cell(row=nu_st,column=nu_cmn,value=val)
    f_xlsx.save(out)  
 ```
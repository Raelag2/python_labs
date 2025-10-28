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
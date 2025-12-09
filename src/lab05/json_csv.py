from pathlib import Path
import json
import csv

def csv_2_json(samples: str, out: str|Path = None, encoding='utf-8'):
    spisok = []
    
    with open(samples, encoding='utf-8') as csv_fi:
        filtr = csv.DictReader(csv_fi)
        for li1 in filtr:
            spisok.append(li1)
    
    if validate_csv(spisok) == False:
        raise TypeError

    if out is None:
        samples = Path(samples)
        diroput = Path('data\out')
        out = diroput / f'people_from_csv.json'

    with open(out,'w',encoding='utf-8') as json_fi:
        json.dump(spisok, json_fi, ensure_ascii=False)

def validate_json(data):
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, dict):
            return False

def validate_csv(data):
    if not isinstance(data, list):
        return False
    for row in data:
        if not isinstance(row, list):
            return False
        
'''
def validate_json(data):
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                return True
    else: return False
'''

def json_2_csv(samples: str, out: str|Path = None, encoding = 'utf-8'):
    with open(samples, 'r', encoding='utf-8') as json_fi:
        filtr = json.load(json_fi)
    
    if validate_json(filtr) == False:
        raise TypeError

    if out is None:
        samples = Path(samples)
        diroput = Path('data\out')
        out = diroput / f'people_from_json.csv'

    with open(out,'w',encoding='utf-8',newline='') as csv_fi:
        head = filtr[0].keys()
        pisa = csv.DictWriter(csv_fi, fieldnames=head)
        pisa.writeheader()
        pisa.writerows(filtr)
from pathlib import Path
import json
import csv

def csv_2_json(puta: str|Path, outputa: str|Path = None, encoding='utf-8'):
    tester = []

    with open(puta, encoding='utf-8') as csv_fi:
        red = csv.DictReader(csv_fi)
        for li1 in red:
            tester.append(li1)
    
    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'{puta.stem}.json'


    with open(outputa,'w',encoding='utf-8') as json_fi:
        json.dump(tester, json_fi, ensure_ascii=False, indent=2)


def json_2_csv(puta: str|Path, outputa: str|Path = None, encoding = 'utf-8'):
    with open(puta, 'r', encoding='utf-8') as json_fi:
        blue = json.load(json_fi)
    
    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'{puta.stem}.csv'

    with open(outputa,'w',encoding='utf-8',newline='') as csv_fi:
        head = blue[0].keys()
        pisa = csv.DictWriter(csv_fi, fieldnames=head)
        pisa.writeheader()
        pisa.writerows(blue)
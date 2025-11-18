from pathlib import Path
from openpyxl import *
import csv 

def csv_2_xlsx(puta: str|Path, outputa: str|Path = None, encoding='utf-8'):
    nig = Workbook()
    lis = nig.active
    lis.title = 'Заголовок'

    if outputa is None:
        puta = Path(puta)
        diroputa = Path('data\output_stuff')
        outputa = diroputa / f'people.xlsx'

    with open(puta,'r') as csv_fi:
        red = csv.reader(csv_fi)
        for nu_st, lin in enumerate(red,1):
            for nu_cmn, val in enumerate(lin,1):
                lis.cell(row=nu_st,column=nu_cmn,value=val)
    nig.save(outputa)  


an = csv_2_xlsx('src\lab05\pupa.csv',encoding='utf-8') 
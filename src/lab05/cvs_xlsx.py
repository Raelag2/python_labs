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
 